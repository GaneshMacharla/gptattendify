from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import UserDetails,StudentData,AttendanceCode
import random
import string
from django.contrib import messages
from django.contrib.auth.models import User
from Accounts.models import Profile
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO

def generate_code():
    code = ''.join(random.choices(string.digits, k=6))
    expiry_date = timezone.now() + timezone.timedelta(minutes=10)
    return AttendanceCode.objects.create(code=code, expiry_date=expiry_date)
    

def display_code(request):
    #get the lecturer name and some extra information through POST method
    user=request.user
    branch=request.POST.get("branch")
    semester=request.POST.get("semester")
    shift=request.POST.get("shift")
    subject=request.POST.get("subject")                                             
    #generate code
    code=generate_code()
    remaining_time = code.expiry_date-timezone.now()
    remaining_time = max(remaining_time, timedelta(0))  # Ensure remaining_time is not negative
   
    info=UserDetails()
    info.user=user
    info.branch=branch
    info.semester=semester
    info.shift=shift
    info.subject=subject
    info.created_date=timezone.now()
    info.expiry_date=code.expiry_date
    info.code=str(code.code)
    info.save()
    return render(request,'Attendance/takeattendance.html',{'code':code,'remaining_time':remaining_time})
 
def take_attendance(request):
    return render(request,'Attendance/takeattendance.html',{'code':None,'reamining_time':None})

def show_attendance_status(request, code):
    students_present = StudentData.objects.filter(code=code)
    lecturer = UserDetails.objects.get(user=request.user, code=code)

    # Create a buffer to hold the PDF data
    buffer = BytesIO()

    # Create a PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Create a table to hold the present students data
    data = [['Name', 'Pin', 'Subject', 'Shift', 'Semester', 'Branch']]
    for student in students_present:
        data.append([student.fullname, student.pin, lecturer.subject, lecturer.shift, lecturer.semester, lecturer.branch])

    # Add style to the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table = Table(data)
    table.setStyle(style)

    # Add table to elements
    elements.append(table)

    # Build the PDF document
    doc.build(elements)

    # Get PDF data from buffer
    pdf_data = buffer.getvalue()
    buffer.close()

    # Create an HTTP response with PDF content
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="present_students_{code}.pdf"'

    return response



def mark_attendance(request):
    return render(request,'Attendance/markattendance.html')


def attendance_validation(request):
    lecturer_username=request.POST.get("username")
    branch=request.POST.get("branch")
    semester=request.POST.get("semester")
    shift=request.POST.get("shift")
    subject=request.POST.get("subject")
    code=request.POST.get("code")
    pin=request.POST.get("pin")
    user=None
    try:
        user=User.objects.get(username=lecturer_username)
        lecturer= UserDetails.objects.get(user=user,code=code)
        
    except Exception:
        messages.error(request,"please enter valid lecturer username")
        return redirect('mark-attendance')
    if timezone.now()>lecturer.expiry_date:
        messages.error(request,"you are not allowed to mark your attendance,because the code has expired it's validity.")
        return redirect('mark-attendance')
    if branch!=lecturer.branch:
        messages.error(request,"please enter valid branch..")
        return redirect('mark-attendance')
    if semester!=lecturer.semester:
        messages.error(request,"please enter valid semester..")
        return redirect('mark-attendance')
    if shift!=lecturer.shift:
        messages.error(request,"please enter valid shift(I/II)")
        return redirect('mark-attendance')
    if subject!=lecturer.subject:
        messages.error(request,"please enter valid subject name ")
        return redirect('mark-attendance')
    if code!=lecturer.code:
        messages.error(request,"please enter a valid 6 digit code")
        return redirect('mark-attendance')
    
    student=StudentData()
    user_profile = get_object_or_404(Profile, user=request.user)
    student.code=code
    student.fullname=user_profile.fullname
    student.pin=pin
    if StudentData.objects.filter(code=code,fullname=user_profile.fullname).exists():
        messages.error(request,"You already have been marked your attendance")
        return redirect('mark-attendance')
    student.save()
    return redirect('attendance-sucessful-message')

def attendance_sucessful_message(request):
    return render(request,'Attendance/attendancesucessful.html',{'username':request.user})
