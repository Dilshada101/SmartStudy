from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import *

def feature1_page(request):
    return render(request, 'StudyPortal/feature.html')

def hello_feature1(request):
    return HttpResponse("Hello from Feature 1 branch")

def about_page(request):
    return render(request, 'StudyPortal/about.html')

def admin_dashboard_view(request):
    User = get_user_model()  
    stats = {
        'users': User.objects.count(),
        'books': Book.objects.count(),
        'assignments': Assignment.objects.count(),
        'courses': Course.objects.count(),
    }

    
    recent_users = User.objects.order_by('-date_joined')[:6]       
    recent_courses = Course.objects.order_by('-id')[:6]             

    context = {
        'stats': stats,
        'recent_users': recent_users,
        'recent_courses': recent_courses,
    }

    return render(request, 'admin/dashboard.html', context)
