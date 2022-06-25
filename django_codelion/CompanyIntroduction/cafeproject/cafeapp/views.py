from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def detail(request):
    return render(request, 'portfolio-details.html')

def mmm(request):
    return render(request, 'mmm.html')