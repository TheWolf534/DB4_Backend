from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField()
    concentration = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class BoardParameters(models.Model):
    boardNumber = models.FloatField()
    targetTemperature = models.FloatField()
    proportional = models.FloatField()
    integral = models.FloatField()
    derivative = models.FloatField()
