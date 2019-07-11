from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,unique=True)
    address = models.CharField(max_length=255)
    dob = models.CharField(max_length=50)
    m_no = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email


