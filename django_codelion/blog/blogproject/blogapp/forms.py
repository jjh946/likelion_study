from django import forms
from .models import Blog

class BlogForm(forms.Form):
    #내가 입ㄱ력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__al__'
        fields = ['title', 'body']