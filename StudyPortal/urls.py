from django.contrib import admin
from django.urls import path
from StudyPortal.views import admin_dashboard_view
from .import views
urlpatterns = [
    path('about/', views.about_page, name='about_page'), 
    path('feature1/', views.feature1_page, name='feature1_page'),
    path('admin/dashboard/', admin.site.admin_view(admin_dashboard_view), name='dashboard'),
    path('admin/',admin.site.urls),
]