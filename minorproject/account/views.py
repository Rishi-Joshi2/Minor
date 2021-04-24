from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass2']

        user = auth.authenticate(username = email,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials *_*')
            return render(request,'account/login.html')
    else:
        return render(request,'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']        
        username = request.POST['email']
        if User.objects.filter(username = username).exists():
            messages.info(request,'An Account with this email already exist *_*')
            return render(request,'account/register.html')
        if len(username)==0:
            messages.info(request,'No Username entered _')
            return render(request,'account/register.html')
        
        email = request.POST['email']
        password = request.POST['pass2']
        user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.profile.gender = getGender(request.POST['gender'])
        fi = getDate(request.POST['birthday'])
        user.profile.birth_date = fi
        user.save()
        
        return render(request,'account/login.html')
    else:
        return render(request,'account/register.html')



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