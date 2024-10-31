# Create Models for Sensors and Temperature Data

from django.db import models
from django.contrib.auth.models import User

class Sensor(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class TemperatureData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
