from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class product_category(models.Model):
    cat_name=models.CharField(max_length=20)
    cat_description=models.CharField(max_length=100, default="Null")
    cat_pic = models.ImageField(default='categories/test12.jpg',null=True,blank=True ,upload_to = 'categories')
    def __str__(self):
        return self.cat_name

class product(models.Model):
    medicinename=models.CharField(max_length=40)
    productdescription=models.TextField(default="NULL",null=True)
    keyingr=models.TextField(default="NULL",null=True)
    cat_id=models.ForeignKey(product_category, on_delete=models.CASCADE)
    prescriptiontype = (('T','True'),('F','False'))
    productpic = models.ImageField(null=True,blank=True ,upload_to = 'products')
    prescriptionreq = models.TextField(max_length=50, choices = prescriptiontype ,blank=True)
    mrp=models.IntegerField()
    medquantity=models.IntegerField()
    meduses=models.TextField(max_length=80, null=True, default="NULL")
    safetyinfo=models.TextField(default="NULL",null=True)
    brand=models.CharField(max_length=100,null=True ,default="NULL")
    manufracturer=models.CharField(max_length=100 ,default="NULL", null=True)


    def __str__(self):
        return self.medicinename
    
class cart(models.Model):
    cus_id=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.cus_id.first_name

    @property
    def get_total_cart(self):
        return self.quantity * self.product_id.mrp


class order(models.Model):
    cus_id=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address_ordered = models.TextField(max_length=150)
    pincode_ordered = models.CharField(max_length=15)
    date_ordered = models.DateTimeField()
    STATUS_CHOICE = (('Accepted','Accepted'),('Packed','Packed'),('On the Way','On the Way'),('Delivered','Delivered'),('Canceled','Canceled'),('Pending','Pending'))
    status = models.CharField(max_length=50, choices = STATUS_CHOICE ,default='Pending')