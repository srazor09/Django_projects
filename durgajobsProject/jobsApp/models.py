from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    eligibility=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    phonenumber=models.IntegerField()

class punejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    eligibility=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    phonenumber=models.IntegerField()

class bangljobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    eligibility=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    phonenumber=models.IntegerField()

class chennjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    eligibility=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    phonenumber=models.IntegerField()
