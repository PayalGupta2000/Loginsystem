from django.forms import PasswordInput
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages,auth
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    return render(request,"home.html")


def signup(request):
    if request.user.is_authenticated:
        return render(request,"home.html")
    else:
        if request.method=="POST":
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            
            confirm_password=request.POST['confirm_password']
            if password==confirm_password:
                if Users.objects.filter(username=username).exists():
                    messages.info(request,"Username is already exits.")
                    return redirect('message')
                elif Users.objects.filter(email=email).exists():
                    messages.info(request,"email already exists.")
                    return redirect('message')
                else:
                    user=Users.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                    user.save()
                    return redirect('/')
            else:
                messages.warning(request,"password do not match.")
                return redirect('message')
        else:
            return render(request,"signup.html")
    
def login(request):
    if request.user.is_authenticated:
        return render(request,"home.html")
    else:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
        
            else:
                messages.info(request,"invalid credentials.")
                return redirect('/')
        else:
            return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def message(request):
    return render(request,"message.html")