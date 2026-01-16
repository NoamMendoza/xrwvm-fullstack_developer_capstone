# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
# - Name
    name = models.CharField(max_length=50)
# - Description
    description = models.TextField()
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}"


class CarModel(models.Model):
# - Many-To-One relationship to Car Make model (One Car Make has many
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
# Car Models, using ForeignKey field)
# - Name
    name = models.CharField(max_length=50)
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('TRUCK', 'Truck')
    ]
    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default='SEDAN'
    )
# - Year (IntegerField) with min value 2015 and max value 2023
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )
# - Any other fields you would like to include in car model
    color = models.CharField(max_length=20, blank=True)
# - __str__ method to print a car make object
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
