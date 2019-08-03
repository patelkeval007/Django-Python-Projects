from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="adminpanel"),

    path('show_user/', views.show_user, name="show_user"),
    path('update_user_page/', views.update_user_page, name="update_user_page"),
    path('update_user/', views.update_user, name="update_user"),
    path('del_user/', views.del_user, name="del_user"),

    path('show_supplier/', views.show_supplier, name="show_supplier"),
    path('add_supplier_view_page/', views.add_supplier_view_page, name="add_supplier_view_page"),
    path('add_supplier/', views.add_supplier, name="add_supplier"),
    path('update_supplier_page/', views.update_supplier_page, name="update_supplier_page"),
    path('update_supplier/', views.update_supplier, name="update_supplier"),
    path('del_supplier/', views.del_supplier, name="del_supplier"),

    path('show_category/', views.show_category, name="show_category"),
    path('add_category/', views.add_category, name="add_category"),
    path('del_category/', views.del_category, name="del_category"),

    path('show_color/', views.show_color, name="show_color"),
    path('add_color/', views.add_color, name="add_color"),
    path('del_color/', views.del_color, name="del_color"),

    path('show_design/', views.show_design, name="show_design"),
    path('add_design/', views.add_design, name="add_design"),
    path('del_design/', views.del_design, name="del_design"),
    path('upload_design_csv/', views.upload_design_csv, name="upload_design_csv"),

    path('show_product/', views.show_product, name="show_product"),
    path('add_product_view_page/', views.add_product_view_page, name="add_product_view_page"),
    path('add_product/', views.add_product, name="add_product"),
    path('update_product_page/', views.update_product_page, name="update_product_page"),
    path('update_product/', views.update_product, name="update_product"),
    path('del_product/', views.del_product, name="del_product"),

    path('show_sales/', views.show_sales, name="show_sales"),
    path('update_sales_page/', views.update_sales_page, name="update_sales_page"),
    path('update_sales/', views.update_sales, name="update_sales"),
    path('del_sales/', views.del_sales, name="del_sales"),

    path('show_stock/', views.show_stock, name="show_stock"),
    path('show_out_stock/', views.show_out_stock, name="show_out_stock"),

    path('show_report/', views.show_report, name="show_report"),
    path('show_report_stock/', views.show_report_stock, name="show_report_stock"),
    path('stock_overall_pdf/', views.stock_overall_pdf, name="stock_overall_pdf"),
    path('stock_month_pdf/', views.stock_month_pdf, name="stock_month_pdf"),
    path('users_pdf/', views.users_pdf, name="users_pdf"),
    path('users_excel/', views.users_excel, name="users_excel"),

]
