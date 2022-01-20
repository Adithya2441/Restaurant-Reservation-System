from asyncio.windows_events import NULL
import re
from django.shortcuts import render ,redirect
from .models import *
from django.contrib import messages



def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        obj = Register.objects.all()
        list = []
        for i in obj:
            list.append(i.username)
        if username not in list:
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if password1==password2:
                obj=Register(username=username,email=email,password1=password1,password2=password2)
                obj.save()
            else:
                messages.error(request,'Password doesnot match')
                return redirect('login')
        else:
            messages.error(request,'Username already exists')
            return redirect('login')
    return render(request,'login.html')

def authenticate_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        obj=Register.objects.get(username=username)
        try:
            if obj is not None:
                if obj.password1==password:
                    messages.success(request,'Logged In Successfully')
                    return redirect('main_page')
                else:
                    messages.error(request,'Invalid Password')
                    return redirect('login')
            else :    
                messages.error(request,'Username doesnot exist')
                return redirect('login')
        except:
            return render(request,'authenticate_login.html')
    return render(request,'authenticate_login.html')

def main_page(request):
    list = Restaurant.objects.all()
    context ={
        'restaurants' : list
    }
    return render(request,'text.html',context)
