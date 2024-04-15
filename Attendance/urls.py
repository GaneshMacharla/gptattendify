from django.urls import path
from  . import views


urlpatterns=[
    path('generate-code',views.display_code,name="generate-code"),
    path('take-attendance',views.take_attendance,name="take-attendance"),
    path('show-attendance-status',views.show_attendance_status,name="show-attendance-status"),
    path('mark-attendance',views.mark_attendance,name="mark-attendance"),
]
