from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
from django.http import HttpResponse


def main(request):
    return render(request,'main.html')

from django.conf import settings
def map(request):
    content = {
        'naver':settings.NAVER_MAP_CLIENT_ID
    }
    return render(request,'map.html', content)



from django.contrib.auth import login,logout
def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = UserCreateForm()
    return render(request,'create_user.html',{'form':form})