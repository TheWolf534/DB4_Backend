from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import SensorData
from django.views.decorators.csrf import csrf_exempt
from .serializer import SensorDataSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
import json


@csrf_exempt
def rule_api(request):

    pass

class SensorDataListCreate(generics.ListCreateAPIView):
    serializer_class = SensorDataSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return SensorData.objects.all()
    
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

def test(request):
    return JsonResponse({'status': 'success'})

def receive_sensor_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sensor_data = SensorData(
            temperature=data['temperature'],
            concentration=data['concentration']
        )
        sensor_data.save()
        return JsonResponse({'status': 'success'}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_data_points(request):
    data_points = request.GET.get('data_points')
    
    if data_points not in [field.name for field in SensorData._meta.fields]:
        return HttpResponseBadRequest(f'Invalid data points: {data_points}')
    
    data_values = SensorData.objects.values_list(data_points, flat=True)
    data_list = list(data_values)
    return JsonResponse({data_points: data_list})

def get_latest_data_point(request):
    data_points = request.GET.get('data_points')

    
    if data_points not in [field.name for field in SensorData._meta.fields]:
        return HttpResponseBadRequest(f'Invalid data point: {data_points}')
    
    data_values = SensorData.objects.values_list(data_points, flat=True)
    data_list = list(data_values)
    return SensorData.objects.filter(id__lt=SensorData.objects.latest('id').id)
    try:
        return JsonResponse({data_points: data_list[-1]})
    except IndexError:
        return JsonResponse({data_points: None})    
