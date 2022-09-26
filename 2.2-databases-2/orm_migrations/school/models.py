from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя', blank=True, null=True)
    subject = models.CharField(max_length=10, verbose_name='Предмет', blank=True, null=True)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя', blank=True, null=True)
    teachers = models.ManyToManyField(Teacher, related_name='student')
    group = models.CharField(max_length=10, verbose_name='Класс', blank=True, null=True)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name
