from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FingerPrint(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    fingerprint=models.CharField(max_length=100)

class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    fullname=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/',default='images/avatar7.png')

    def __str__(self) -> str:
        return f'{self.username} profile'

        