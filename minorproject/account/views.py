from typing import ContextManager
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Profile
from main.models import *
# Create your views here.

def logReg(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    return render(request, 'account/login,register.html')

def user_information(request):
    user = request.user
    if user.is_authenticated:
        context = {'user':user}
        return render(request,'account/user-information.html',context)
    else:
        return redirect('login')


def login(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass2']
        
        user = auth.authenticate(username = email,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials *_*')
            return render(request,'account/login,register.html')
    else:
        return render(request,'account/login,register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['email']
        if User.objects.filter(username = username).exists():
            messages.info(request,'An Account with this email already exist *_*')
            return render(request,'account/login,register.html')
        if len(username)==0:
            messages.info(request,'No Username entered *_*')
            return render(request,'account/login,register.html')
        
        email = request.POST['email']
        password = request.POST['pass2']
        
        # user.profile.gender = getGender(request.POST['gender'])
        
        fi = int(request.POST['phnum'])

        try:
            check_phnum = Profile.objects.get(phone_number = fi)
            messages.info(request,'User with this phone number already exist *_*')
            print(check_phnum)
            return render(request,'account/login,register.html')
        except:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)    
            user.profile.phone_number = fi

        user.save()
        
        return render(request,'account/login,register.html')
    else:
        return render(request,'account/login,register.html')



def getDate(s):
    sp = s.split('/')
    sp.reverse()
    listToStr = '-'.join([str(elem) for elem in sp])
    return listToStr

def getGender(s):
    if s == 'Male':
        return 'M'
    else:
        return 'F'


def address(request):
    user = request.user
    if user.is_authenticated:
        context = {'user':user}
        return render(request,'account/addresses.html',context)
    else:
        return redirect('login')

def edit_address(request):
    user = request.user
    if user.is_authenticated:
        address1 = request.POST['address1']
        pincode1 = request.POST['Pincode1']
        address2 = request.POST['address2']
        pincode2 = request.POST['pincode2']

        if len(address2) != 0:
            user.profile.address2 = address2

        if len(pincode2) != 0:
            user.profile.pincode2 = pincode2

        if len(address1) != 0:
            user.profile.address1 = address1
        else:
            messages.info(request,'Null value not accepeted in address 1 field')
            return redirect('address')

        if len(pincode1) != 0:
            user.profile.pincode1 = pincode1
        else:
            messages.info(request,'Null value not accepeted in pincode 1 field')
            return redirect('address')


        user.save()

        context = {'user':user}
        return redirect('address')
    else:
        return redirect('login')

def invoices(request):
    user = request.user
    if user.is_authenticated:
        order_history = order.objects.filter(cus_id = user)
        print(order_history)

        amount = 0
        cart_product = [p for p in cart.objects.all() if p.cus_id == request.user]

        for p in cart_product:
            tempamount = (p.quantity*p.product_id.mrp)
            amount+=tempamount

        totalpurchased = len(cart_product)

        context = {'order_history':order_history,'totalpurchased':totalpurchased,'user':user}
        return render(request,'account/invoices.html',context)
    else:
        return redirect('login')