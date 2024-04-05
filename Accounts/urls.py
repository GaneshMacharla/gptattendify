from django.urls import path
from  . import views

urlpatterns=[
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup_user,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('user-profile-view/',views.profile_view,name='user-profile-view'),
    path('user-profile-edit/',views.profile_edit,name="user-profile-edit"),
    path('edit-profile-image/',views.edit_profile_image,name="edit-profile-image"),
    path('user-profile-edit-save/',views.user_profile_edit_save,
    name="user-profile-edit-save")
]



