from django.contrib import admin

from .models import *

class orderAdmin(admin.ModelAdmin):
    list_display = ('cus_id','product_id','quantity','address_ordered','date_ordered','status')
    list_editable = ('status',)
    search_fields = ('cus_id__email',)
    list_filter = ('date_ordered',)

class productAdmin(admin.ModelAdmin):
    list_display = ('medicinename','productdescription','productpic','mrp','medquantity','manufracturer')
    list_editable = ('productdescription','productpic','mrp','medquantity')
    search_fields = ('medicinename',)

admin.site.register(cart)
admin.site.register(product,productAdmin)
admin.site.register(product_category)
admin.site.register(order, orderAdmin)