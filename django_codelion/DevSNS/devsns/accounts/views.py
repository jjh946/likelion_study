from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) #해당하는 유저가 있다면 유저객체를 반환하고 만약 그렇지 않다면 none을 반환한다

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')


    #로그인 시키기
    else:
        return render(request, 'login.html')
    # request == GET
    # login html 띄우기
    
def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'register.html')
    return render(request, 'login.html')