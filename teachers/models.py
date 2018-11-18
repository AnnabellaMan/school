from django.db import models


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=128)
    teacher_passport = models.CharField(max_length=10)
    teacher_phone = models.CharField(max_length=48)
    teacher_address = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    education = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    classroom = models.CharField(max_length=128)
    mastering = models.CharField(max_length=128)
    salary = models.CharField(max_length=128)




