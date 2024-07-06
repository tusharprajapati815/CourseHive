from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, redirect
from App.models import Course, Videos, UserCourse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def mycourses(request):
    user = request.user
    user_course = UserCourse.objects.filter(user = user)
    context = {
        'user_course' : user_course
    }
    return render(request, 'my_courses.html', context=context)

def coursePage(request, slug):
    print(request.user.is_authenticated)
    print(slug)
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    videos = course.videos_set.all().order_by("serial_no")
    next_lecture = 2
    prev_lecture = None

    if serial_number is None:
        serial_number = 1
    else:
        next_lecture = int(serial_number) + 1
        if len(videos) < next_lecture:
            next_lecture = None
        
        prev_lecture = int(serial_number) - 1

    video = Videos.objects.get(serial_no = serial_number, Course = course)

    if(video.is_preview is False):

        if(request.user.is_authenticated is False):
            return redirect('login')
        #check if the logged user has purchased the course or not
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user, course = course)
            except:
                return redirect('checkoutpage', slug = course.slug)

    #if you are enrolled in this course you can watch any videos.

    print(video)
    d = {'course': course, 'video': video, 'videos': videos, 'nextlecture': next_lecture, 'prevlecture': prev_lecture}
    return render(request, 'coursepage.html', context=d)