from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate


def main(request):
    return render(request,'main.html')

from django.conf import settings
def map(request):
    content = {
        'naver':settings.NAVER_MAP_CLIENT_ID
    }
    return render(request,'map.html', content)


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
        else:
            raise ValueError('오류 발생')
    else:
        form = UserCreateForm()
    return render(request,'create_user.html',{'form':form})

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email = email, password = password)
        
        if user.is_valid():
            login(request, user)
            return redirect('main')
        else:
            raise ValueError('아이디와 비밀번호가 다릅니다.')
    return render(request, 'login.html')


def user_logout(request):
    
    logout(request)
    return redirect('main')
    
