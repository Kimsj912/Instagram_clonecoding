from django.db import models
from django.db.models.fields import CharField, EmailField, IntegerField

class userInfo(models.Model):
    email = models.EmailField(max_length=254)
    phoneNum = models.CharField(max_length=50)
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    password = models.CharField(max_length=50)