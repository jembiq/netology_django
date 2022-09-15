# coding=utf-8

from django.db import models


class Book(models.Model):
    name = models.CharField(u'Название', max_length=64, blank=True, null=True)
    author = models.CharField(u'Автор', max_length=64, blank=True, null=True)
    pub_date = models.DateField(u'Дата публикации', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True, max_length=64)

    def __str__(self):
        return f'{self.name} {self.author}'
