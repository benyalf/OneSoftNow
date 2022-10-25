from django.shortcuts import render


def current_datetime(request):
    
    return render(request, "home/base.html")