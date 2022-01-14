from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth import authenticate,login
from django.contrib import messages

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        obj=Register(username=username,email=email,password1=password1,password2=password2)
        obj.save()
    return render(request,'login.html')

def authenticate_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        obj=Register.objects.get(username=username)
        if obj.password1==password:
            messages.success(request,f'{username} logged in')
            return redirect(request,'main_page')
        else:
            messages.error(request,'Invalid User')
            return redirect(request,'login')
    else :
        return render(request,'login.html')
        
def main_page(request):
    return render(request,'text.html')
