from django.shortcuts import render, redirect, get_object_or_404
from cafeapp.forms import CartMenuForm

from cafeapp.models import Cafe, CartMenu, Menu

def home(request):
    cafes = Cafe.objects.all()
    return render(request, 'index.html',{'cafes':cafes})
'''
def home(request):
    cafes = Cafe.objects.all()
    return render(request, 'index.html',{'cafes':cafes})
'''

def detail(request):
    return render(request, 'portfolio-details.html')


'''
def mmm(request, cafe_id):
    cafe_detail = get_object_or_404(Cafe, pk=cafe_id)
    return render(request, 'mmm.html', {'cafe_detail':cafe_detail})
'''
def mmm(request):
    return render(request, 'mmm.html')

def mypage(request):
    return render(request, 'mypage.html')

def done(request):
    return render(request, 'done.html')

def gift(request):
    return render(request, 'gift.html')

def gift2(request):
    return render(request, 'gift2.html')






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

def add(request, post_id):
    menu_add = get_object_or_404(Menu, pk=post_id)
    return render(request, 'add.html', {'menu_add':menu_add})

def payment(request):
    if request.method == 'POST' or request.method == 'FILES':
        return redirect('done')
    else:
        cartmenus = CartMenu.objects.filter().order_by('-date')
        sum = 0
        for menu in cartmenus:
            sum += menu.price
        return render(request, 'payment.html', {'cartmenus':cartmenus,'sum':sum})

