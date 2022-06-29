from django.shortcuts import render, redirect
from cafeapp.forms import CartMenuForm

from cafeapp.models import CartMenu, Menu

def home(request):
    return render(request, 'index.html',)
    

def detail(request):
    return render(request, 'portfolio-details.html')

def mmm(request):
    return render(request, 'mmm.html')


def order(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = CartMenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order', )
    #request method가 post일 경우
        #입력값 저장

    #request method가 get일 경우
    else:
        menus = Menu.objects.filter().order_by('date')
        cartmenus = CartMenu.objects.filter().order_by('-date')
        sum = 0
        for cartmenu in cartmenus:
            sum += cartmenu.price
        return render(request, 'order.html', {'posts':cartmenus,'sum':sum, 'menus':menus})

def add(request):
    return render(request, 'add.html')

def payment(request):
    if request.method == 'POST' or request.method == 'FILES':
        
        return redirect('order')
    #request method가 post일 경우
        #입력값 저장

    #request method가 get일 경우
    else:
        menus = CartMenu.objects.filter().order_by('-date')
        sum = 0
        for menu in menus:
            sum += menu.price
        return render(request, 'payment.html', {'sum':sum})

def gift(request):
    return render(request, 'gift.html')

def gift2(request):
    return render(request, 'gift2.html')
