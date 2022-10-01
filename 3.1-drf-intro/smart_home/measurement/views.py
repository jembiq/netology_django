# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from http.client import SERVICE_UNAVAILABLE
from rest_framework.views import APIView
from rest_framework.response import Response

from measurement import serializers
from .models import Measurement, Sensor

from django.shortcuts import redirect


def index(request):
    return redirect('api/')

class SensorAPIView(APIView):
    def get(self, request):
        measures = Measurement.objects.all()
        sensors = Sensor.objects.all()
        serializer = serializers.SensorDetailSerializer(sensors, many=True)
        return Response(serializer.data)

    