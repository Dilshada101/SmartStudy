from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),               # Home page
    path('about/', views.about, name='about'),       # About page
    
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup_view, name='signup'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("submit-assignment/<int:assignment_id>/", views.submit_assignment, name="submit_assignment"),

    # Optional: Features
    path('feature1/', views.feature1_page, name='feature1_page'),

    # Optional: File handling
    path('view/<str:type>/<int:file_id>/', views.view_file, name='view_file'),
    path('download/<str:type>/<int:file_id>/', views.download_file, name='download_file'),
    
    # AI Assistant
    path('chat/', views.chat_page, name='chat'),
    path('chat/api/prompt/', views.chat_api, name='chat_api'),
    path('chat/api/generate_ppt/', views.generate_ppt_api, name='generate_ppt_api'),
]

