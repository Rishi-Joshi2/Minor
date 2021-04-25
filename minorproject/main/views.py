from django.shortcuts import render
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
