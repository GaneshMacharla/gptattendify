from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FingerPrint(models.Model):

    username=models.ForeignKey(User,on_delete=models.CASCADE)
    fingerprint=models.CharField(max_length=100)

    
