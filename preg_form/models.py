from django.db import models

# Create your models here.
class reg_tb(models.Model):
    fname=models.CharField(max_length=128,default='')
    lname=models.CharField(max_length=128,default='')
    dptm=models.CharField(max_length=128,default='')
    stream=models.CharField(max_length=128,default='')
    username=models.CharField(max_length=128,default='')
    password=models.CharField(max_length=128,default='')
    email=models.CharField(max_length=128,default='')
    mob_no=models.CharField(max_length=128,default='')

