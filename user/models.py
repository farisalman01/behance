from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    dp=models.ImageField(max_length=200,null=True,blank=True)
    cover=models.ImageField(max_length=200,null=True,blank=True)
    facebook=models.CharField(max_length=200,null=True,blank=True)
    twitter=models.CharField(max_length=200,null=True,blank=True)
    linkedln=models.CharField(max_length=200,null=True,blank=True)


    def __str__(self):
        return self.name






