from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .models import *
from django.shortcuts import render,redirect
from django.contrib import messages
from StudyPortal.forms import RegistrationForm
from django.shortcuts import get_object_or_404
from django.http import FileResponse, HttpResponse
import mimetypes
import os

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'register.html')
        
        
        context = {
            'username': username,
            'email': email,
            'password': password,  
            'confirm_password': confirm_password
        }
        return render(request, 'result.html', context)

    return render(request, 'register.html')

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
def assignment_dashboard(request):
    return render(request, 'admin/custom_assignments.html')

def notes_dashboard(request):
    return render(request, 'admin/custom_notes.html')

def resources_dashboard(request):
    return render(request, 'admin/custom_resources.html')

def progress_dashboard(request):
    return render(request, 'admin/custom_progress.html')

def course_dashboard(request):
    return render(request, 'admin/custom_course.html')


def get_model_by_type(file_type):
    if file_type == 'assignment':
        return Assignment
    elif file_type == 'note':
        return Note
    elif file_type == 'resource':
        return Resource
    else:
        return None


def view_file(request, type, file_id):
    model = get_model_by_type(type)
    obj = get_object_or_404(model, id=file_id)
    file_path = obj.file.path

    # Serve file inline for viewing
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'inline; filename="{os.path.basename(file_path)}"'
    return response


def download_file(request, type, file_id):
    model = get_model_by_type(type)
    obj = get_object_or_404(model, id=file_id)
    file_path = obj.file.path

    # Set response for download
    mime_type, _ = mimetypes.guess_type(file_path)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type=mime_type)
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response







