# Generated by Django 4.1.1 on 2022-09-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_phone_lte_exists_alter_phone_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
