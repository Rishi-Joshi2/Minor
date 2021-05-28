from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import *
import json
from django.db.models import Q
from datetime import datetime

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
    amount = 0
    cart_product = [p for p in cart.objects.all() if p.cus_id == request.user]

    for p in cart_product:
        tempamount = (p.quantity*p.product_id.mrp)
        amount+=tempamount

    totalpurchased = len(cart_product)

    context={'products1':products1,'totalpurchased':totalpurchased}
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
    
def cart1(request):
    user = request.user
    if user.is_authenticated:
        try:
            c = cart.objects.filter(cus_id = request.user)
        except:
            print("cart query not matched")
            c = None
        
        
        print(c)
        amount = 0
        cart_product = [p for p in cart.objects.all() if p.cus_id == request.user]

        for p in cart_product:
            tempamount = (p.quantity*p.product_id.mrp)
            amount+=tempamount

        totalpurchased = len(cart_product)
        data = {
            'totalpurchased':totalpurchased,
            'amount':amount
        }
        data['cart'] = c
        print(data['cart'])
        return render(request,'main/cart.html',data)
    else:
        return redirect('login')

def categories(request):
    cat = product_category.objects.all()
    products1=filtering_out_data_category_wise()
    print(products1)
    # temp1 = {}
    # for i in products1:
    #     temp = product_category.objects.get(cat_name = i)
    #     temp1[temp.cat_name]=(temp.id)
    cart_product = [p for p in cart.objects.all() if p.cus_id == request.user]
    # print(temp1)

    totalpurchased = len(cart_product)
    
    context={'cat':cat,'products1':products1,'totalpurchased':totalpurchased}
    return render(request,'main/shop-categories.html',context)

def product_details(request,pk):
    product_information = product.objects.get(pk = pk)
    prod_cat = product.objects.filter(cat_id=product_information.cat_id)
    print(prod_cat)
    amount = 0
    cart_product = [p for p in cart.objects.all() if p.cus_id == request.user]

    for p in cart_product:
        tempamount = (p.quantity*p.product_id.mrp)
        amount+=tempamount

    totalpurchased = len(cart_product)

    
    context = {'product_information':product_information,'totalpurchased':totalpurchased,'prod_cat':prod_cat}
    return render(request,'main/product-default.html',context)

def add_to_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        product_information = product.objects.get(pk = prod_id)
        print(product_information)
        user = request.user
        try:
            c = cart.objects.get(cus_id = request.user,product_id=product_information)
        except:
            print("cart query not matched")
            c = None
        
        print(c)
        if c:
            c.quantity+=1
            c.save()
        else:
            cont_obj = cart(cus_id = user,product_id=product_information, quantity=1)
            cont_obj.save()
            c = cart.objects.get(cus_id = user,product_id=product_information)
        amount = 0
        cart_product = [p for p in cart.objects.all() if p.cus_id == request.user]

        sumofitem = c.get_total_cart
        for p in cart_product:
            tempamount = (p.quantity*p.product_id.mrp)
            amount+=tempamount

        totalpurchased = len(cart_product)
        data = {
            'sumofitem': sumofitem,
            'quantity':c.quantity,
            'totalpurchased':totalpurchased,
            'amount':amount
        }
    # print("\U0001f600")
    return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        product_information = product.objects.get(pk = prod_id)
        print(product_information)
        user = request.user
        try:
            c = cart.objects.get(cus_id = user,product_id=product_information)
        except:
            print("cart query not matched")
            c = None
        
        print(c)
        if c:
            c.quantity-=1
            c.save()
        else:
            cont_obj = cart(cus_id = user,product_id = product, quantity=1)
            cont_obj.save()
            c = cart.objects.get(product_id=prod_id,cus_id = request.user)

        try:
            test = cart.objects.filter(cus_id = request.user)
            print("this is also working",test)
            for i in test:
                print(i,i.quantity)
                if i.quantity == 0:
                    print("deleting:-",i.product_id.medicinename)
                    i.delete()
        except:
            print("hehehehe")

        amount = 0
        cart_product = [p for p in cart.objects.all() if p.cus_id == request.user]

        for p in cart_product:
            tempamount = (p.quantity*p.product_id.mrp)
            amount+=tempamount

        totalpurchased = len(cart_product)
        data = {
            'quantity':c.quantity,
            'totalpurchased':totalpurchased,
            'amount':amount
        }
    return JsonResponse(data)

def removecart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        product_information = product.objects.get(pk = prod_id)
        print(product_information)
        user = request.user
        try:
            c = cart.objects.get(cus_id = request.user,product_id=product_information)
        except:
            print("cart query not matched")
            c = None
        
        print(c)
        if c:
            c.delete()
        amount = 0
        cart_product = [p for p in cart.objects.all() if p.cus_id == request.user]

        for p in cart_product:
            tempamount = (p.quantity*p.product_id.mrp)
            amount+=tempamount

        totalpurchased = len(cart_product)
        data = {
            'totalpurchased':totalpurchased,
            'amount':amount
        }
    return JsonResponse(data)

def category(request,catid):
    print(catid)
    try:
        spe = product_category.objects.get(pk=catid)
    except:
        return render(request,'main/404-page.html')
    print(spe)
    products_details = product.objects.filter(cat_id=spe)
    print(products_details)

    amount = 0
    cart_product = [p for p in cart.objects.all() if p.cus_id == request.user]

    for p in cart_product:
        tempamount = (p.quantity*p.product_id.mrp)
        amount+=tempamount

    totalpurchased = len(cart_product)

    context = {'spe':spe,'value':products_details,'totalpurchased':totalpurchased}
    return render(request,'main/shop-default.html',context)

import razorpay
from django.contrib.sites.shortcuts import get_current_site

def checkout(request):
    user = request.user
    if user.is_authenticated:
        try:
            c = cart.objects.filter(cus_id = request.user)
        except:
            print("cart query not matched")
            c = None
        
        
        print(c)
        amount = 0
        cart_product = [p for p in cart.objects.all() if p.cus_id == request.user]

        for p in cart_product:
            tempamount = (p.quantity*p.product_id.mrp)
            amount+=tempamount

        totalpurchased = len(cart_product)

        final_price = amount

        order_currency = 'INR'

        callback_url = 'http://'+ str(get_current_site(request))+"/handlerequest/"
        print(callback_url)
        notes = {'order-type': "basic order from the website", 'key':'value'}
        temp = "workplease"
        razorpay_client = razorpay.Client(auth=('rzp_test_OrSWAaMq9arlUq', 'fjmPCsbhR7rTduZmLIhlapCh'))
        razorpay_order = razorpay_client.order.create(dict(amount=final_price*100, currency=order_currency, notes = notes, receipt=temp, payment_capture='0'))
        print(razorpay_order['id'])
        final_amount2 = amount*100
        data = {
            'totalpurchased':totalpurchased,
            'amount':amount,
            'order_id': razorpay_order['id'], 
            'orderId':temp, 
            'final_price':final_price, 
            'callback_url':callback_url,
            'final_amount2':final_amount2
        }
        data['cart'] = c
        print(data['cart'])
        return render(request,'main/checkout.html',data)
    else:
        return redirect('login')



from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def handlerequest(request):
    if request.method == "POST":
        user =request.user

        c = cart.objects.filter(cus_id = request.user)
        d=datetime.now()
        for i in c:
            
            x = order(cus_id=user, product_id=i.product_id,quantity=i.quantity,address_ordered=user.profile.address1,pincode_ordered=user.profile.pincode1,date_ordered=d)
            x.save()
            i.delete()

        return redirect('/account/invoices')

def autocomplete(request):
    if request.is_ajax():
        res = None
        product_name = request.POST.get('product_name')
        print(product_name)
        ps = product.objects.filter(medicinename__icontains = product_name)
        print(ps)
        if len(ps) > 0 and len(product_name)>0:
            data = []
            for pos in ps:
                item={
                    'pk':pos.pk,
                    'name':pos.medicinename,
                    'img':str(pos.productpic.url)
                }
                data.append(item)
            res = data
        else:
            res = 'No result found...'

        return JsonResponse({'data':res})
    return JsonResponse({})

def searched(request):
    if request.method == "POST":
        amount = 0
        cart_product = [p for p in cart.objects.all() if p.cus_id == request.user]

        for p in cart_product:
            tempamount = (p.quantity*p.product_id.mrp)
            amount+=tempamount

        totalpurchased = len(cart_product)

        searched_query = request.POST.get('product')
        print(searched_query)
        ps = product.objects.filter(medicinename__icontains = searched_query)
        context = {'value':ps,'totalpurchased':totalpurchased}
    else:
        not_found = "Get request is not accepted"
        context = {'value':not_found}
    return render(request,'main/shop-default.html',context)