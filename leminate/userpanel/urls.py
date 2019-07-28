from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="userpanel"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    path('product_detail/', views.product_detail, name="product_detail"),
    path('product_add_to_cart/', views.product_add_to_cart, name="product_add_to_cart"),

    path('shoping_cart/', views.shoping_cart, name="shoping_cart"),
    path('product_remove_from_cart/', views.product_remove_from_cart, name="product_remove_from_cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('show_myaccount/', views.show_myaccount, name="show_myaccount"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('show_change_pass/', views.show_change_pass, name="show_change_pass"),
    path('edit_password/', views.edit_password, name="edit_password"),
]
