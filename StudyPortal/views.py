from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def feature1_page(request):
    return render(request, 'StudyPortal/feature.html')

def hello_feature1(request):
    return HttpResponse("Hello from Feature 1 branch")

def about_page(request):
    return render(request, 'StudyPortal/about.html')