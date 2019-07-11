from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="adminpanel"),
    path('show_user/', views.show_user, name="show_user"),
    path('update_user_page/', views.update_user_page, name="update_user_page"),
    path('update_user/', views.update_user, name="update_user"),
    path('del_user/', views.del_user, name="del_user"),
]
