from django.urls import path
from . import views
urlpatterns = [
    path('about/', views.about_page, name='about_page'), 
    path('feature1/', views.feature1_page, name='feature1_page'),

]