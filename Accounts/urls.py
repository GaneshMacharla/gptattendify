from django.urls import path
from  . import views

urlpatterns=[
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup_user,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('profile-view/',views.profile_view,name='profile-view'),
    path('profile-update/',views.profile_update,name="profile-update"),
    path('profile-picture-update/',views.profile_picture_update,name="profile-picture-update"),
    path('profile-update-save/',views.profile_update_save,name="profile-update-save"),
]

