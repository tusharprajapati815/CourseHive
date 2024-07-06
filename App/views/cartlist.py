from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from App.models import Cart, Course, UserCourse, Payment
from django.urls import reverse
from django.contrib import messages 
from project.settings import *
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from time import time
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def addcart(request, cid):
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message': 'User does not exist'})

    user = request.user

    try:
        course = Course.objects.get(id=cid)
    except Course.DoesNotExist:
        return render(request, 'error.html', {'message': 'Course does not exist'})
    
    course = Course.objects.get(id=cid)
    c = Cart()
    c.course =  course
    c.user = user
    c.save()
    messages.success(request,'Your Product Added in Cart')
    return redirect('/')

def calculate_discounted_price(price, discount):
    return price - (price * discount * 0.01)

import razorpay

client = razorpay.Client(auth = (KEY_ID, SECRET_KEY))

def cart_list(request):
    if not request.user.is_authenticated:
        login_url = reverse('login')
        next_url = reverse('cartlist')
        return redirect(f'{login_url}?next={next_url}')
    
    user = request.user
    action = request.GET.get('action')
    cart_items = Cart.objects.filter(user=user)
    order = None
    error = None

    for item in cart_items:
        item.discounted_price = calculate_discounted_price(item.course.price, item.course.discount)

    total_paise = sum(item.discounted_price for item in cart_items) * 100
    total_rupees = total_paise // 100

    if action == "create_payment":
        payment_errors = []
        for item in cart_items:
            currency = "INR"
            notes = {
                "email": user.email,
                "name": f'{user.username}'
            }
            receipt = f"project-{int(time())}"
            amount = int(item.discounted_price * 100)  # Amount for individual course

            try:
                order = client.order.create(
                    {
                        'receipt': receipt,
                        'notes': notes,
                        'amount': amount,
                        'currency': currency
                    }
                )

                payment = Payment()
                payment.user = user
                payment.course = item.course
                payment.order_id = order.get('id')
                payment.save()
            except Exception as e:
                payment_errors.append(str(e))

        if payment_errors:
            error = "Some payments could not be processed: " + ", ".join(payment_errors)
        else:
            # Redirect to checkout page or success page
           return redirect('success')

    return render(request, 'cartlist.html', context={
        'cart_items': cart_items,
        'total_rupees': total_rupees,
        'total_paise': total_paise,
        'order': order,
        'error': error
    })

@csrf_exempt
def success_view(request):
    if request.method == 'POST':
        data = request.POST
        context = {}
        try:
            # Verification logic would go here
            # If verification is successful, render the success template
            return render(request, 'success.html', context)
        except:
            return HttpResponse("Invalid Payment Details")
    else:
        # If it's not a POST request, just render the success template
        return render(request, 'success.html')
        
        
def Delete_Cartitem(request,id):
    cart=Cart.objects.get(id=id)
    cart.delete()
    messages.error(request,'Your Product removed From Cart Sucessfully')     
    return redirect('/cartlist')

