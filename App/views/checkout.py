from django.shortcuts import render, HttpResponse, redirect
from App.models import Course, Videos, Payment, UserCourse
from project.settings import *
from time import time
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import razorpay
client = razorpay.Client(auth = (KEY_ID, SECRET_KEY))
# Create your views here.

@login_required(login_url='/login')
def checkOut(request, slug):
    course = Course.objects.get(slug = slug)

    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    error = None
    
    try:
        user_course = UserCourse.objects.get(user = user, course = course)
        error = 'You are Already Enrolled in this Course'
    except:
        pass

    amount = None
    if error is None:    
        amount = int((course.price - (course.price * course.discount * 0.01)) * 100)

    # if amount is zero dont create payment, only save enrollment object
    if amount == 0:
        userCourse = UserCourse(user = user, course = course)
        userCourse.save()
        return redirect('my-courses')

    

    if action == "create_payment":
        currency = "INR"
        notes = {
            "email" : user.email,
            "name" : f'{user.username}'
        }
        receipt = f"project-{int(time())}"
        order = client.order.create(
            {
            'receipt' : receipt, 
            'notes' : notes, 
            'amount' : amount, 
            'currency' : currency
            }
        )

        payment = Payment()
        payment.user = user
        payment.course = course
        payment.order_id = order.get('id')
        payment.save()

    return render(request, 'check_out.html', context={'course': course, 
            'order': order, 
            'payment': payment,
            'user': user,
            'error': error})

@csrf_exempt
def verifyPayment(request):
    if request.method == 'POST':
        data = request.POST
        context = {}
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']  #square bracket is used if there is a issue in payment then exception can be raised. 
            razorpay_payment_id = data['razorpay_payment_id']

            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            userCourse = UserCourse(user = payment.user, course = payment.course)
            userCourse.save()

            payment.user_course = userCourse

            payment.save()

            return redirect('my-courses')
        except:
            return HttpResponse("Invalid Payment Details")
        