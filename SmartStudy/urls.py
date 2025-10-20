from django.contrib import admin
from django.urls import path
from StudyPortal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/customprogress/', views.custom_progress_view, name='customprogress'),
]
