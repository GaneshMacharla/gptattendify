from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class AttendanceCode(models.Model):
    code=models.CharField(max_length=10,unique=True)
    expiry_date=models.DateTimeField()

    def is_valid(self):
        return self.expiry_date>timezone.now()

class UserDetails(models.Model):
    #Lecturer
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    semester=models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    shift=models.CharField(max_length=200)
    code=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    created_date=models.DateTimeField()
    expiry_date=models.DateTimeField()

    def __str__(self)->str:
        return self.code
    

class StudentData(models.Model):
    code=models.CharField(max_length=6)
    fullname=models.CharField(max_length=200)
    pin=models.CharField(max_length=200)

    def __str__(self):
        return self.fullname


