from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import SensorData, BoardParameters
from django.views.decorators.csrf import csrf_exempt
from .serializer import SensorDataSerializer, BoardParametersSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
import json


@csrf_exempt
def rule_api(request):

    pass

class SensorDataListCreate(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

class LatestSensorData(generics.ListAPIView):
    serializer_class = SensorDataSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return SensorData.objects.order_by("-timestamp")[:1]

class BoardParametersListCreate(generics.CreateAPIView, generics.RetrieveUpdateAPIView):
    queryset = BoardParameters.objects.all()
    serializer_class = BoardParametersSerializer
    permission_classes = [AllowAny]
    lookup_field = 'boardNumber'


    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)