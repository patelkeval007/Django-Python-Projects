from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="login"),
    path('authenticate_user_login/', views.authenticateUserLogin, name="authenticate_user_login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('forgot_password/', views.forgotPassword, name="forgot_password"),
    path('authenticateUserRegistration/', views.authenticateUserRegistration, name="authenticateUserRegistration"),
    path('sendOTP/', views.sendOTP, name="sendOTP"),
    path('change_password/', views.change_password, name="change_password"),
    path('check_change_pass/', views.check_change_pass, name="check_change_pass"),
]
