from django.contrib import admin
from .models import AttendanceCode,UserDetails,StudentData
# Register your models here.

admin.site.register(AttendanceCode)
admin.site.register(UserDetails)
admin.site.register(StudentData)

