from django.shortcuts import render,redirect
from .models import *


def filtering_out_data_category_wise():
    data = product.objects.all()
    proid = product_category.objects.all()
    liproname = []
    mydict = {}
    for i in proid:
        liproname.append(i.cat_name)

    for j in liproname:
        temp = []
        for k in data:
            if(k.cat_id.cat_name==j):
                temp.append(k)        
        mydict[j] = temp
    print(mydict)
    return mydict

def home(request):
    products1=filtering_out_data_category_wise()
    print(products1)
    context={'products1':products1}
    return render(request,'main/index.html', context)

# Create your views here.

def aboutus(request):
    return render(request,'main/about-us.html')

def policy(request):
    return render(request,'main/policy.html')

def termsCondition(request):
    return render(request,'main/terms-condition.html')

def shipping(request):
    return render(request,'main/policy.html')

def contactUs(request):
    return render(request,'main/contact-us.html')
    
def cart(request):
    user = request.user
    if user.is_authenticated:
        return render(request,'main/cart.html')
    else:
        return redirect('login')

def checkout(request):
    user = request.user
    if user.is_authenticated:
        context = {'user':user}
        return render(request,'main/checkout.html',context)
    else:
        return redirect('login')

def categories(request):
    cat = product_category.objects.all()
    products1=filtering_out_data_category_wise()
    print(products1)
    context={'cat':cat,'products1':products1}
    return render(request,'main/shop-categories.html',context)

def product_details(request,pk):
    product_information = product.objects.get(pk = pk)
    prod_cat = product.objects.filter(cat_id=product_information.cat_id)
    print(prod_cat)

    context = {'product_information':product_information}
    return render(request,'main/product-default.html',context)