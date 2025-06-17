from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longtitude = models.DecimalField(max_digits=9, decimal_places=6)
    rating = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)