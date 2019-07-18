from django.contrib import admin
from .models import User,Category,Color,Design,Product,Supplier,SalesOrder,SalesOrderDetail
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
