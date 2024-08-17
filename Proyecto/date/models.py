from django.db import models
from client.models import Client


# Create your models here.
class DateVehicle(models.Model):
    tradeMark = models.CharField(max_length=50)
    vehicleModel = models.CharField(max_length=50)
    year = models.IntegerField()
    numberDoors = models.IntegerField()
    parking = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    vehicleType = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='vehicles/')


class Date(models.Model):
    DateVehicle = models.ForeignKey(DateVehicle, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    daydate = models.DateField(null=True)
