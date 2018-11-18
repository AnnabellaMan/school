from django.db import models
from teachers.models import Teacher


class Student(models.Model):
    student_name = models.CharField(max_length=128)
    parent_name = models.CharField(max_length=128)
    parent_passport = models.CharField(max_length=10)
    student_passport = models.CharField(max_length=10)
    student_SNILS = models.CharField(max_length=48)
    parent_phone = models.CharField(max_length=48)
    student_address = models.CharField(max_length=128)
    class_number = models.CharField(max_length=128)
    form_master = models.CharField(max_length=128)




