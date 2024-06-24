from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField()
    concentration = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class BoardParameters(models.Model):
    boardNumber = models.IntegerField()
    targetTemperature = models.FloatField()
    targetRPM = models.FloatField()
    motorDirection = models.CharField(max_length=10, default='FORWARD')
    TempProportional = models.FloatField(default=0.0)
    TempIntegral = models.FloatField(default=0.0)
    TempDerivative = models.FloatField(default=0.0)
    ODProportional = models.FloatField(default=0.0)
    ODIntegral = models.FloatField(default=0.0)
    ODDerivative = models.FloatField(default=0.0)
