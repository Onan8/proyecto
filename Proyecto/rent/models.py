from django.db import models


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
