from django.db import models
from django.utils import timezone
# Create your models here.

class AttendanceCode(models.Model):
    code=models.CharField(max_length=10,unique=True)
    expiry_date=models.DateTimeField()
  

    def is_valid(self):
        return self.expiry_date>timezone.now()

