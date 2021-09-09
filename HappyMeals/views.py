from django.shortcuts import render,HttpResponse,redirect
from HappyMeals.models import customer
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
def index(request):
    return render(request,'index.html')

def sign_in (request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('./order')
        else:    
            return redirect('./sign_in')
    return render(request,'signin.html')            
   
def sign_up(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        info =customer(date =datetime.today(),name=name,email=email,password=password,phone=phone,address=address)
        info.save()   
    return render(request,'signup.html')
def order(request):
    return render(request,'order.html')    
       

