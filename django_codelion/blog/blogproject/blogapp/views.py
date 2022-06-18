from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone

def home(request):
    return render(request, 'index.html')

#블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

#블로그 글을 저장해준는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')