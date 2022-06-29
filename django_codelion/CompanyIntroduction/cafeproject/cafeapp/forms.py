from django import forms
from .models import CartMenu

class CartMenuForm(forms.ModelForm):
    class Meta:
        model = CartMenu
        #fields = '__all__'
        fields = ['title', 'price']