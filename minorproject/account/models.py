from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICE = (('M','MALE'),('F','FEMALE'))
    
    gender = models.TextField(max_length=50, choices = GENDER_CHOICE ,blank=True)
    birth_date = models.DateField(auto_now_add=False,auto_now=False, blank=True,null=True)
    
    #profile_pic = models.ImageField(default='profile1.jpg',null=True,blank=True)

    def __str__(self):
        return self.user.first_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()