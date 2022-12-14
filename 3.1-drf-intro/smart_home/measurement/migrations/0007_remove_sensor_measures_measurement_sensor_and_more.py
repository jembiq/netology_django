# Generated by Django 4.1.1 on 2022-10-01 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_remove_measurement_sensor_id_sensormeasurements_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='measures',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='measure', to='measurement.sensor'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
