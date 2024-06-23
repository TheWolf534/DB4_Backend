from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import SensorData, BoardParameters
from django.views.decorators.csrf import csrf_exempt
from .serializer import SensorDataSerializer, BoardParametersSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import generics, status
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

class BoardParametersRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = BoardParameters.objects.all()
    serializer_class = BoardParametersSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        board_number = self.kwargs.get('boardNumber')
        if not board_number:
            raise NotFound('boardNumber field is required.')

        try:
            instance = BoardParameters.objects.get(boardNumber=board_number)
        except BoardParameters.DoesNotExist:
            raise NotFound('BoardParameters with the specified boardNumber does not exist.')

        return instance


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        try:
            instance = self.get_object()
        except NotFound:
            # If the instance does not exist, create a new one
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
