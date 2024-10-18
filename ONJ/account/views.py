from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login, logout, authenticate
import json
import requests

def main(request):
    return render(request,'main.html')

from django.conf import settings
def map(request):
    
    return render(request,'map.html')
def map_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
           
            kakao_api_url =  "https://apis-navi.kakaomobility.com/v1/waypoints/directions"
            headers = {
                'Content-Type':'application/json',
                'Authorization':"KakaoAK fa733b63db3616a945bbaea4996a5085"
            }
            response = requests.post(kakao_api_url, headers=headers, json=data)
            return JsonResponse(response.json())
        except json.JSONDecodeError:
            return JsonResponse({'error':'유효하지 않은 json'}, status=400)
        except requests.RequestException as e:
            return JsonResponse({"error": str(e)},status=500)
    else:
        return JsonResponse({"error":'POST방식이 아닙니다.'},status=405)


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
    
