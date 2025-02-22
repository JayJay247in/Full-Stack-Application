# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CarMake(models.Model):
    """
    Represents a car make (e.g., Toyota, Honda, Ford).
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Car Make")
        verbose_name_plural = _("Car Makes")


class CarModel(models.Model):
    """
    Represents a specific car model (e.g., Corolla, Civic, Mustang).
    """
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='car_models')
    dealer_id = models.IntegerField()  # Refers to a dealer in Cloudant
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')  # Increased max_length
    year = models.IntegerField(
        default=2023,  # Set the current year as the default
        validators=[
            MaxValueValidator(2024),  # Use current year + 1 for future entry
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"

    class Meta:
        verbose_name = _("Car Model")
        verbose_name_plural = _("Car Models")