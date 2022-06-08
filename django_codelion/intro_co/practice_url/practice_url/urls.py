from django.contrib import admin
from django.urls import path
from jojoapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('second/', views.second)
]
