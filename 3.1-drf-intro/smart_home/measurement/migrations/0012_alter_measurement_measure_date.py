# Generated by Django 4.1.1 on 2022-10-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0011_alter_measurement_measure_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measure_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
