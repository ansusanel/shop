from django.db import models

# Create your models here.
class Ordetable(models.Model):    
    ProductName=models.CharField(max_length=20)    
    ProductPrice=models.FloatField()
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Number=models.IntegerField()

class Feedbacktable(models.Model):
    UserName=models.CharField(max_length=20)
    Email=models.EmailField()
    Message=models.CharField(max_length=50)

class Registrationtable(models.Model):
    UserName=models.CharField(max_length=20,default='')
    Email=models.EmailField()
    Password=models.CharField(max_length=10,default='')      
 
