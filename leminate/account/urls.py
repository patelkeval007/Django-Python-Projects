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
]
