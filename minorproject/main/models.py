from django.db import models
from django.contrib.auth.models import User
#images yet to be added and product category me fields shubham se confirm karna hai 
#orders class to be formed

class product_category(models.Model):
    cat_name=models.CharField(max_length=20)
    cat_description=models.CharField(max_length=100, default="Null")
    def __str__(self):
        return self.cat_name

class product(models.Model):
    medicinename=models.CharField(max_length=40)
    cat_id=models.ForeignKey(product_category, on_delete=models.CASCADE)
    prescriptiontype = (('T','True'),('F','False'))
    
    prescriptionreq = models.TextField(max_length=50, choices = prescriptiontype ,blank=True)
    mrp=models.IntegerField()
    medquantity=models.IntegerField()
    meduses=models.CharField(max_length=80, null=True, default="NULL")
    def __str__(self):
        return self.medicinename
class cart(models.Model):
    cust_id=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(product, on_delete=models.CASCADE)
    def __str__(self):
        return self.cust_id.first_name


