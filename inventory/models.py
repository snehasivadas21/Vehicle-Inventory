from django.db import models

# Create your models here.

class Vehicle(models.Model):
    class Fueltype(models.TextChoices):
        PETROL = "Petrol","Petrol"
        DIESEL = "Diesel","Diesel"
        ELECTRIC = "Electric","Electric"
        HYBRID = "Hybrid","Hybrid"
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10,decimal_places=2)
    fuel_type = models.CharField(max_length=20,choices=Fueltype.choices)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,related_name="booking")
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.customer_name} - {self.vehicle}"



