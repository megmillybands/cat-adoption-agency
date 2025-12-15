from django.db import models

AVAILABILITY = {
    'AV': 'Available',
    'OH': 'On Hold',
    'NA': 'Not Available',
}
GENDER = {
    'M': 'Male',
    'F': 'Female',
}

class Profile(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

class Cat(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER)
    breed = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    availability = models.CharField(max_length=2, choices=AVAILABILITY)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=250, blank=True)