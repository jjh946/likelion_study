from calendar import c
from django.contrib import admin
from .models import CartMenu, Menu, Cafe


# Register your models here.
admin.site.register(CartMenu)
admin.site.register(Menu)
admin.site.register(Cafe)