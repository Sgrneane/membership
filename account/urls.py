from django.contrib import admin
from django.urls import path

from . import views

app_name='account'
urlpatterns = [
    path('login',views.login_user,name='login_user'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout_user,name='logout_user'),
    path('activate',views.activate, name='activate'),
    path('resend_token',views.resend_token,name='resend_token'),
    path('my-profile',views.my_account,name="my_account"),
    path('change-password',views.change_password,name='change_password')
]