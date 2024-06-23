from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField()
    concentration = models.FloatField()
    rpm = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class BoardParameters(models.Model):
    boardNumber = models.IntegerField()
    targetTemperature = models.FloatField()
    targetRPM = models.FloatField()
    targetDirection = models.BooleanField(default=False)
    proportional = models.FloatField()
    integral = models.FloatField()
    derivative = models.FloatField()
