from django.db import models

# Create your models here.
class Clients(models.Model):
    name=models.CharField(max_length=30)
    adress=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)

class Articles(models.Model):
    name=models.CharField(max_length=30)
    type=models.CharField(max_length=20)
    price=models.IntegerField()

class Request(models.Model):
    number=models.IntegerField()
    date=models.DateField()
    status=models.BooleanField()
