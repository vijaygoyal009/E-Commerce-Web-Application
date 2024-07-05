from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.

   


def login_page1(request):
   try: 
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
    else:
        print('ok')
    if not User.objects.filter(username=username):
       messages.error(request,'invalid user name') 
    user=authenticate(username=username,password=password)
    if user is None:
         messages.error(request,'Invalid') 
    else:
        login(request,user)
        return redirect('/')
   except Exception as e:
    print(e)
       
   return render(request,'login1.html')
def logout_page(request):
    logout(request)
    return redirect('/account/login/')


def login_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get("password")
        user =User.objects.filter(username=username)
        if  User.objects.filter(username=username):
            messages.error(request,"user already exists")
            return redirect('/account/login1/')
        else:
          user =User.objects.create(first_name=first_name,
                                  last_name=last_name,
                                  email=email,
                                  username=username)
          user.set_password(password)
          user.save()
          return redirect('/')
        

    else:
        print("nothing happend")

    return render(request,'login.html')
