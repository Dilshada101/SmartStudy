from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.custom_progress_view, name='customprogress'),
]
