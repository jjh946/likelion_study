from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),

    #html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    #django ford을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    #django modelform을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),
]
