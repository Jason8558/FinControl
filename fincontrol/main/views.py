from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

def loginform(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user=user)
            return redirect('/')
    return render(request, 'main/login.html')

def index(request):
    if not request.user.is_authenticated:
        return loginform(request)
    return render(request, 'main/index.html', context={'username':request.user.first_name})


    
