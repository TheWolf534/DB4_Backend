from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField()
    concentration = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

