from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255, unique=True)
    identity = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    telephone = models.CharField(max_length=15, unique=True)
    license = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.name} ({self.email})"