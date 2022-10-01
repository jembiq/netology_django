from dataclasses import field
from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Sensor, Measurement

class SensorMeasurementsInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            form.cleaned_data

        return super().clean()

class SensorMeasurementsInline(admin.TabularInline):
    model = Measurement
    formset = SensorMeasurementsInlineFormset

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    inlines = [SensorMeasurementsInline]

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'measure_date']
