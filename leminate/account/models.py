from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    dob = models.CharField(max_length=50)
    m_no = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    m_no = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Design(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    qoh = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=255)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)
    design_id = models.ForeignKey(Design, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SalesOrder(models.Model):
    address = models.CharField(max_length=255)
    date = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    # user_id= models.BigIntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.name + '-' + self.date


class SalesOrderDetail(models.Model):
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales_order_id = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)

    def __str__(self):
        return self.sales_order_id.user_id.name + '-' + self.sales_order_id.date + '-' + self.product_id.name


class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.name


class CartDetail(models.Model):
    quantity = models.IntegerField(default=0)
    date_add = models.CharField(max_length=50)
    total = models.IntegerField(default=0)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.cart_id.user_id.name
