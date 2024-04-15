from django.shortcuts import render,redirect,HttpResponse
from django.utils import timezone
from .models import AttendanceCode
from datetime import timedelta
import random
import string

def generate_code():
    code = ''.join(random.choices(string.digits, k=6))
    expiry_date = timezone.now() + timezone.timedelta(seconds=5)
    return AttendanceCode.objects.create(code=code, expiry_date=expiry_date)
    

def display_code(request):
    print(request.user)
    branch=request.POST.get("branch")
    semester=request.POST.get("semester")
    shift=request.POST.get("shift")
    subject=request.POST.get("subject")
    print(branch)
    print(semester)
    print(shift)
    print(subject)

    code=generate_code()
    remaining_time = code.expiry_date-timezone.now()
    remaining_time = max(remaining_time, timedelta(0))  # Ensure remaining_time is not negative
    return render(request,'Attendance/takeattendance.html',{'code':code,'remaining_time':remaining_time})
 
def take_attendance(request):
    return render(request,'Attendance/takeattendance.html',{'code':None,'reamining_time':None})


def show_attendance_status(request):
    return render(request,'Attendance/showattendancestatus.html')

def mark_attendance(request):
    return render(request,'Attendance/markattendance.html')

