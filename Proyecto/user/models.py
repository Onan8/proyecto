from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo Email debe ser establecido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    number_employee = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    number_id = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)

    # Configuración de campos de autenticación
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'number_employee']

    # Opciones del modelo
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.name} ({self.number_employee})"
