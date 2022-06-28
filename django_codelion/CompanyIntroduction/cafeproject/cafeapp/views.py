from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def detail(request):
    return render(request, 'portfolio-details.html')

def mmm(request):
    return render(request, 'mmm.html')


def order(request):
    return render(request, 'order.html')

def gift(request):
    return render(request, 'gift.html')

def gift2(request):
    return render(request, 'gift2.html')