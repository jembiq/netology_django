# Generated by Django 4.1.1 on 2022-09-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_measure_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measure_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
