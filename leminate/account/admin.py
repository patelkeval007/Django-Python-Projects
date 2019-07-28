from django.contrib import admin
from .models import User, Category, Color, Design, Product, Supplier, SalesOrder, SalesOrderDetail, Cart, CartDetail,Stock

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Design)
admin.site.register(Product)
# admin.site.register(ProductImage)
admin.site.register(Supplier)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderDetail)
admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(Stock)
