from dataclasses import fields
from django.db import models
# from django.forms.fields import ImageField

class Sensor(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return f'{self.id}: {self.name}'


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measure', blank=True, null=True)
    measure_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=True)
    temperature = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to='uploads/')
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return str(self.measure_date)

