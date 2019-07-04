from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="login"),
    path('authenticate_user/', views.authenticateUser, name="authenticate_user"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
]
