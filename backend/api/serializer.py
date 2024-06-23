from rest_framework import serializers
from .models import SensorData, BoardParameters

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ["id", "temperature", "concentration","timestamp"]

class BoardParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardParameters
        fields = ["id", "boardNumber", "targetTemperature","proportional","integral","derivative"]