from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def feature1_page(request):
    return render(request, 'StudyPortal/feature.html')

def hello_feature1(request):
    return HttpResponse("Hello from Feature 1 branch")

def about_page(request):
    return render(request, 'StudyPortal/about.html')


User = get_user_model()

@login_required
def dashboard_view(request):
    user = request.user

    # Default context
    context = {"stats": {}, "recent_courses": [], "recent_users": []}

    # ================== ADMIN DASHBOARD ==================
    if user.is_staff:
        context["stats"] = {
            "users": User.objects.count(),
            "courses": Course.objects.count(),
            "assignments": Assignment.objects.count(),
            "notes": Note.objects.count(),
        }
        context["recent_courses"] = Course.objects.order_by("-id")[:5]
        context["recent_users"] = User.objects.order_by("-id")[:5]

    # ================== TEACHER DASHBOARD ==================
    elif user.groups.filter(name="Teacher").exists():
        context["stats"] = {
            "overall": User.objects.count(),  # Example stat
            "assigned_tasks": Assignment.objects.filter(teacher=user).count(),
            "add_note": Note.objects.filter(teacher=user).count(),
            "progress": Progress.objects.filter(teacher=user).count(),
        }

    # ================== STUDENT DASHBOARD ==================
    else:
        context["stats"] = {
            "assignments": Assignment.objects.filter(student=user).count(),
            "notes": Note.objects.filter(student=user).count(),
            "books": Book.objects.count(),  # all books available
            "progress": Progress.objects.filter(student=user).first().percentage
                        if Progress.objects.filter(student=user).exists()
                        else 0,
        }

    return render(request, "admin/dashboard.html", context)
