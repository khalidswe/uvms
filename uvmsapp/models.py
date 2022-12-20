from datetime import date, datetime
from distutils.command.upload import upload
import email
from email.policy import default
from statistics import mode
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

class Student(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    student_id = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    department = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    pic = models.ImageField(upload_to="app/img/student")

class Officials(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    officials_id = models.CharField(max_length=150)
    department = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    pic = models.ImageField(upload_to="app/img/officials")