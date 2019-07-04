from django.db import models


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email
