from django.urls import path

from measurement.views import SensorAPIView

urlpatterns = [
    path('', SensorAPIView.as_view())
]
