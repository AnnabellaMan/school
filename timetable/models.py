from django.db import models


class Timetable(models.Model):
    class_number = models.CharField(max_length=128)
    classroom = models.CharField(max_length=128)
    teacher = models.CharField(max_length=128)
    day_of_the_week = models.CharField(max_length=128)
    lesson_number = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)




