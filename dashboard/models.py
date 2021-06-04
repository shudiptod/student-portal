from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.TextField(null=True)
    paid = models.IntegerField(null=True)
    payable = models.IntegerField(null=True)
    due = models.IntegerField(null=True)
    otherdue = models.IntegerField(null=True)
    fname = models.TextField(null=True)
    mname = models.TextField(null=True)
    bldgrp = models.TextField(null=True)
    dob = models.DateField(null=True)
    semester = models.TextField(null=True)
    cgpa =models.FloatField(null=True)
            

class Course(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course_code = models.TextField(null=True)
    cname = models.TextField(null=True)
    teachar = models.TextField(null=True)    
