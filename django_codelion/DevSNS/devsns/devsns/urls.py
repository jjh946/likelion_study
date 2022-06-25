from django.contrib import admin
from django.urls import path
from snsapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),
    #127.0.0.1:
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
