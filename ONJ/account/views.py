from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

def main(request):
    return render(request,'base.html')

from django.conf import settings
def map(request):
    content = {
        'naver':settings.NAVER_MAP_CLIENT_ID
    }
    return render(request,'map.html', content)