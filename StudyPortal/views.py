from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import *

def dashboard_view(request):
    return(request, "custom_dahboard.html")
