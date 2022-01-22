from asyncio.windows_events import NULL
from email.headerregistry import Address
import re
from django.shortcuts import render ,redirect
from django.template import context
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
        obj=Register.objects.filter(username=username)
        try:
            if obj is not None:
                if obj[0].password1==password:
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
    list1 = Restaurant.objects.filter(Address='Delhi')
    list2 = Restaurant.objects.filter(Address='Bangalore')
    list3 = Restaurant.objects.filter(Address='Mumbai')
    list4 = Valet.objects.all()
    list5 = Manager.objects.all()
    list6 = []
    for i in list4:
        if i.Manager_ID in list5:
            list6.append(i.Manager_ID)
    
    context ={
        'delhi' : list1,
        'bangalore' : list2,
        'mumbai' : list3,
        'valet_managers' : list6
    }
    return render(request,'text.html',context)

def book_now(request):
    list = Table.objects.all()
    list1 = Restaurant.objects.all()
    context = {
        'tables' : list,
        'restaurants' : list1
    }

    return render(request,'index.html',context)

def menu(request):
    list1 = Menu_Veg.objects.all()
    list2 = Menu_NonVeg.objects.all()
    context = {
        'veg' : list1,
        'nonveg' : list2
    }
    return render(request,'menu.html',context)