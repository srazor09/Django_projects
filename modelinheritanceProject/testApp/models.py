from django.db import models

# Create your models here.
"""  Abstract Inheritance """
class ContactInfo(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    address=models.CharField(max_length=264)

    class Meta:
        abstract=True

class Student(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher(ContactInfo):
    subject=models.CharField(max_length=128)
    salary=models.FloatField()


"""  Multi Table Inheritance """
class ContactInfo1(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    address=models.CharField(max_length=264)

class Student1(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher1(ContactInfo):
    subject=models.CharField(max_length=128)
    salary=models.FloatField()



"""  Multi level inheritance"""
class Parent1(models.Model):
    fd1=models.CharField(max_length=20)
    fd2=models.CharField(max_length=30)

class Child1(Parent1):
    fd3=models.CharField(max_length=30)
    fd4=models.CharField(max_length=30)


class SubChild(Child1):
    fd5=models.CharField(max_length=30)
