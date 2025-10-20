from django.urls import path
from StudyPortal import views

app_name = 'StudyPortal'

urlpatterns = [
    path('about/', views.about_page, name='about_page'), 
    path('feature1/', views.feature1_page, name='feature1_page'),
    path('/register/', views.register, name='register'),
    # path('assignments/', views.assignment_dashboard, name='assignment_dashboard'),

]