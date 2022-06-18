from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

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

# django form을 이ㅇ용해서 입력값을 받는 함수
#get 요청과 (=입력값을 받을 수 있는 html을 갖다 줘야 함)
#post 요청  (=입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리)
# 모두 받을 수 있뜸
def formcreate(request):
    if request.method == 'POST':
        #입력 내용을 db에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        #입력을 받을 수 있는 html을 갖다주기
        form = BlogForm()
    return render(request, 'form_create.html', {'form': form})

def modelformcreate(request):
    if request.method == 'POST':
        
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        #입력을 받을 수 있는 html을 갖다주기
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form': form})