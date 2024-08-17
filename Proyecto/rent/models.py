from django.db import models
from client.models import Client


# Create your models here.
class RentalVehicle(models.Model):
    tradeMark = models.CharField(max_length=50)
    vehicleModel = models.CharField(max_length=50)
    year = models.IntegerField()
    numberDoors = models.IntegerField()
    parking = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    vehicleType = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='vehicles/')


class Rental(models.Model):
    RentalVehicle = models.ForeignKey(RentalVehicle, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dayEntrance = models.DateField(null=True)
    dayExit = models.DateField(null=True
)
