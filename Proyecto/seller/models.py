from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
    number_employee = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255)
    number_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    schedule = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.name} ({self.email})"