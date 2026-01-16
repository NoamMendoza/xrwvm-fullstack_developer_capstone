from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):

    name = models.CharField(max_length=50)

    description = models.TextField()

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}"


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

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

    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )
    color = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
