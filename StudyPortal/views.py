from django.shortcuts import render
from .models import StudentProgress

def custom_progress_view(request):
    progress_data = StudentProgress.objects.all()
    return render(request, 'studyportal/customprogress.html', {'progress_data': progress_data})
