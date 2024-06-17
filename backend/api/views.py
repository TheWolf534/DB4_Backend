from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import SensorData
import json

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

def get_data_point(request):
    data_point = request.GET.get('data_point')
    
    if data_point not in [field.name for field in SensorData._meta.fields]:
        return HttpResponseBadRequest(f'Invalid data point: {data_point}')
    
    data_values = SensorData.objects.values_list(data_point, flat=True)
    data_list = list(data_values)
    return JsonResponse({data_point: data_list})
