"""
URL configuration for SmartStudy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from StudyPortal import views
from StudyPortal import views as study_views




urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('register/', views.register, name= 'register'),
    path('StudyPortal/', include('StudyPortal.urls')),
    path('admin/assignments/', study_views.assignment_dashboard, name='admin_assignment_dashboard'),
    path('admin/notes/', study_views.notes_dashboard, name='admin_notes_dashboard'),
    path('admin/resources/', study_views.resources_dashboard, name='admin_resources_dashboard'),
    path('admin/progress/', study_views.progress_dashboard, name='admin_progress_dashboard'),

]
