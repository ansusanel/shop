from django.db import models

# Create your models here.
class Categorytable(models.Model):
    CategoryName=models.CharField(max_length=20)
    image=models.ImageField(upload_to='imgfolder',default='null.jpg')
    CategoryDescrition=models.CharField(max_length=50)

class Producttable(models.Model):
    CategoryName=models.CharField(max_length=20)
    ProductName=models.CharField(max_length=20)
    image=models.ImageField(upload_to='imgfolder',default='null.jpg')
    ProductDescrition=models.CharField(max_length=50)
    ProductPrice=models.FloatField()