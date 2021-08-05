from django.db import models
from django.db.models.fields import CharField, EmailField, IntegerField
from django.urls import reverse

class userInfo(models.Model):
    email = models.EmailField(max_length=254)
    phoneNum = models.CharField(max_length=50)
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    password = models.CharField(max_length=50)

    def get_absolute_url(self): # redirect시 활용
        return reverse('profile:profile_detail', args=[self.id])