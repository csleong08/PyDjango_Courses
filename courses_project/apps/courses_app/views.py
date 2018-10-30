from django.shortcuts import render, redirect
from time import gmtime, strftime
from django.contrib import messages
from .models import *

def index(request):
    print('INDEX METHOD')
    context = {
        'all_courses' : Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

# def create(request):
#     print('CREATE METHOD')
#     course = Course.objects.create(
#         course_name = request.POST['course_name'],
#         desc = request.POST['desc']
#     )
#     print('CREATE WORKS!')
#     return redirect('/')

def create(request):
    errors= Course.objects.basic_validator(request.POST)
    if len(errors):
        print('IF CREATE')
        for key, value in errors.items():
            messages.error(request, value)
        print("IF WORKS!!")
        return redirect('/')
    else:
        print('ELSE CREATE')
        course = Course.objects.create(
            course_name = request.POST['course_name'],
            desc = request.POST['desc']
        )
        print('ELSE WORKS!')
        return redirect('/')

def show(request, course_id): 
    print('SHOW METHOD')
    context = {
        'course' : Course.objects.get(id=course_id)
    }
    print('SHOW WORKS!')
    return render(request,'courses_app/destroy.html', context)

def destroy(request, course_id):
    print('course_id')
    print('DESTROY METHOD')
    Course.objects.get(id=course_id).delete()
    print('DESTROY WORKS!')
    return redirect('/')

