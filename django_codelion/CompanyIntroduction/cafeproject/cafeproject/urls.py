from django.contrib import admin
from django.urls import path
from cafeapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('mmm/', views.mmm, name='mmm'),
    path('mypage/', views.mypage, name='mypage'),
    path('done/', views.done, name='done'),


    path('login/',accounts_views.login, name='login'),
    path('logout/',accounts_views.logout, name='logout'),

    path('signup/',accounts_views.signup, name='signup'),
    

    path('order/', views.order, name='order'),
    path('payment/', views.payment, name='payment'),
    path('add/', views.add, name='add'),

    path('gift/', views.gift, name='gift'),
    path('gift2/', views.gift2, name='gift2'),
    
]
