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
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from StudyPortal.forms import SubmissionForm
from django.shortcuts import render
from django.http import JsonResponse
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY
OPENAI_API_KEY='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'
def send_message(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '').strip()

        if not user_message:
            return JsonResponse({'message': 'Message cannot be empty'}, status=400)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                ]
            )

            ai_message = response['choices'][0]['message']['content'].strip()
            return JsonResponse({'message': ai_message})

        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)

    return JsonResponse({'message': 'Invalid request'}, status=400)

def chat_view(request):
    return render(request, 'chat/chat.html')




def home(request):
    return render(request, 'home.html')

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

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user_type = request.POST.get("user_type")  # teacher/student

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        user = User.objects.create_user(username=username, email=email, password=password1)

        # Mark teachers as staff (they can access admin panel)
        if user_type == "teacher":
            user.is_staff = True
            user.is_superuser = False
            user.save()

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect("login")

    return render(request, "signup.html")


# ---------- LOGIN ----------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect teachers (staff) to admin panel, students to home page
            if user.is_staff:
                return redirect("/admin/")
            else:
                return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")


# ---------- LOGOUT ----------
def logout_view(request):
    logout(request)
    return redirect("home")

# def signup_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         role = request.POST.get('role')
#         institution_id = request.POST.get('institution')
#         course_id = request.POST.get('course')

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken.")
#             return redirect('signup')

#         user = User.objects.create_user(username=username, email=email, password=password)
#         institution = Institution.objects.filter(id=institution_id).first()
#         course = Course.objects.filter(id=course_id).first()

#         # Create the linked PortalUser
#         PortalUser.objects.create(
#             user=user,
#             role=role,
#             institution=institution
#         )

#         messages.success(request, "Account created successfully! You can now log in.")
#         return redirect('login')

#     institutions = Institution.objects.all()
#     courses = Course.objects.all()

#     return render(request, 'auth/signup.html', {'institutions': institutions}, {'coursess': courses})


# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!")
#             return redirect('dashboard')  # You can adjust this
#         else:
#             messages.error(request, "Invalid username or password.")
#             return redirect('login')

#     return render(request, 'auth/login.html')


# def logout_view(request):
#     logout(request)
#     messages.success(request, "Logged out successfully.")
#     return redirect('login')

def feature1_page(request):
    return render(request, 'StudyPortal/feature.html')

def hello_feature1(request):
    return HttpResponse("Hello from Feature 1 branch")




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


@login_required
def assignment_dashboard(request):
    return render(request, 'admin/custom_assignments.html')


def resources_dashboard(request):
    return render(request, 'admin/custom_resources.html')
def notes_dashboard(request):
    return render(request, 'admin/notes_dashboard.html')

def progress_dashboard(request):
    return render(request, 'admin/progress_dashboard.html')



def course_dashboard(request):
    return render(request, 'admin/custom_course.html')

def user_dashboard(request):
    return render(request, 'admin/custom_user.html')


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
    

@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)

    # ✅ Only students can submit
    if request.user.portaluser.role != "student":
        messages.error(request, "Only students can submit assignments.")
        return redirect("assignments_dashboard")

    # ✅ Get existing submission or create new
    submission, created = Submission.objects.get_or_create(
        assignment=assignment,
        student=request.user.portaluser
    )

    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES, instance=submission)
        if form.is_valid():
            form.save()
            messages.success(request, "Assignment submitted successfully!")
            return redirect("assignments_dashboard")
    else:
        form = SubmissionForm(instance=submission)

    return render(request, "admin/submit_assignment.html", {
        "form": form,
        "assignment": assignment
        })


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

from django.core.mail import send_mail
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            body,
            "no-reply@smartstudy.com",  # Sender
            ["adnanaugust382@gmail.com"],  # Receiver
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        return render(request, "contact.html")

    return render(request, "contact.html")












