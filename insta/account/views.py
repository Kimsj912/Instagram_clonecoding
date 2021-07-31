from django.http.response import HttpResponse
from django.http import HttpResponse
from .forms import UserForm ,LoginForm 
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def login_view(request):
    if request.method=='POST' :
        form = LoginForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None : #user가 존재한다면
            login(request,user)
            return redirect("home")
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else :
        form=LoginForm()
        return render(request, 'login.html', {'form':form})
    
def logout_view(request):
    logout(request)
    return redirect("home")
    
def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
        return redirect('home')
    else :
        form=UserCreationForm()
        return render(request, 'signup.html',{'form':form})