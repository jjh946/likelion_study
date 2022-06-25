from django.contrib import admin
from django.urls import path
from cafeapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('mmm/', views.mmm, name='mmm'),


    path('login/',accounts_views.login, name='login'),
    path('logout/',accounts_views.logout, name='logout'),

    path('signup/',accounts_views.signup, name='signup'),
    
]
