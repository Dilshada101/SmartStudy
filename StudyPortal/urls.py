from django.urls import path
from StudyPortal import views

app_name = 'StudyPortal'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about_page'), 
    path('feature1/', views.feature1_page, name='feature1_page'),
    path('/register/', views.register, name='register'),
    path('view/<str:type>/<int:file_id>/', views.view_file, name='view_file'),
    path('download/<str:type>/<int:file_id>/', views.download_file, name='download_file'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("submit-assignment/<int:assignment_id>/", views.submit_assignment, name="submit_assignment"),
]