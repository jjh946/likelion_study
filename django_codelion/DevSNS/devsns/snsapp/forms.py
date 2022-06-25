from django import forms
from .models import Post, Comment

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        #fields = ['title', 'body']

class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']        