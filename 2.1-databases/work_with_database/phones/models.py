from email.mime import image
from platform import release
from django.db import models
from django.template.defaultfilters import slugify

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    image = models.ImageField(max_length=250, blank=True, null=True)
    release_date = models.DateField(max_length=50, blank=True, null=True)
    lte_exists = models.BooleanField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)
