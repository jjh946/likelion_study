from django.contrib import admin
from django.urls import path
from cafeapp import views
from accounts import views as accounts_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('mypage/', views.mypage, name='mypage'),
    path('done/', views.done, name='done'),


    path('login/',accounts_views.login, name='login'),
    path('logout/',accounts_views.logout, name='logout'),

    path('signup/',accounts_views.signup, name='signup'),
    

    path('order/', views.order, name='order'),
    path('payment/', views.payment, name='payment'),
    path('add/<int:post_id>', views.add, name='add'),

    path('gift/', views.gift, name='gift'),
    path('gift2/<int:post_id>', views.gift2, name='gift2'),
    path('gift3/<int:post_id>', views.gift3, name='gift3'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)