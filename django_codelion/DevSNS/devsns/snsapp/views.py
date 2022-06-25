from django.shortcuts import get_object_or_404, redirect, render
from .forms import Commentform, Postform
from .models import Post

def home(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    #request method가 ost일 경우
        #입력값 저장

    #request method가 get일 경우
    else:
        form = Postform()
    return render(request, 'post_form.html', {'form':form})
        # form 입력 html 띄우기

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = Commentform()
    return render(request, 'detail.html', {'post_detail': post_detail,'comment_form':comment_form})

#댓글 저장
def new_comment(request, post_id):
    filled_form = Commentform(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()

    return redirect('detail', post_id)