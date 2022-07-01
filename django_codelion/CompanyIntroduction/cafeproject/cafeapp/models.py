from django.db import models
from django.contrib.auth.models import User


class CartMenu(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField()
    

    def __str__(self):
        return self.title

class Cafe(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    term = models.CharField(max_length=200)
    
    openState = models.BooleanField()
    myungyul = models.BooleanField()

    def __str__(self):
        return self.title