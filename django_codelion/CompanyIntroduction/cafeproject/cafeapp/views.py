from django.shortcuts import render, redirect, get_object_or_404
from cafeapp.forms import CartMenuForm
from django.utils import timezone
from cafeapp.models import Cafe, CartMenu, Menu

def home(request):
    cafes = Cafe.objects.all()
    return render(request, 'index.html',{'cafes':cafes})


def detail(request, post_id):
    cafe_detail = get_object_or_404(Cafe, pk=post_id)
    return render(request, 'test.html', {'cafe_detail':cafe_detail})

#def detail(request):
 #   return render(request, 'detail.html')

def mypage(request):
    return render(request, 'mypage.html')

def done(request):
    return render(request, 'done.html')

def gift(request):
    return render(request, 'gift.html')

def gift2(request):
    return render(request, 'gift2.html')






def order(request):
        menus = Menu.objects.all()
        cartmenus = CartMenu.objects.filter().order_by('-date')
        sum = 0
        for cartmenu in cartmenus:
            sum += cartmenu.price
        return render(request, 'order.html', {'posts':cartmenus,'sum':sum, 'menus':menus})

def add(request, post_id):
    if request.method == 'POST' or request.method == 'FILES':
        return redirect('order')
    else:
        menus = Menu.objects.all()
        menu_add = get_object_or_404(Menu, pk=post_id)
        post = CartMenu()
        post.title = menu_add.title
        post.price = menu_add.price
        post.save()
        return render(request, 'add.html', {'menus':menus,'menu_add':menu_add})





def payment(request):
    if request.method == 'POST' or request.method == 'FILES':
        return redirect('done')
    else:
        cartmenus = CartMenu.objects.filter().order_by('-date')
        sum = 0
        for menu in cartmenus:
            sum += menu.price
        return render(request, 'payment.html', {'cartmenus':cartmenus,'sum':sum})

