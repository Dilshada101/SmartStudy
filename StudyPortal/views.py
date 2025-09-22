from django.shortcuts import render

def dashboard_view(request):
    return(request, "custom_dahboard.html")
