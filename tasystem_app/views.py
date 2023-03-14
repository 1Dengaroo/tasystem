from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {"title": "Home"}
    return render(request, 'temporary.html', context)

def landing_page(request):
    context = {"title": "Landing Page"}
    return render(request, 'temporary.html', context)

def add_course(request):
    context = {"title": "Add Course"}
    return render(request, 'temporary.html', context)

def course_view(request):
    context = {"title": "Course View"}
    return render(request, 'temporary.html', context)

def apply(request):
    context = {"title": "Apply"}
    return render(request, 'temporary.html', context)