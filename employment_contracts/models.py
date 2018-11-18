from django.db import models


class EmploymentContract(models.Model):
    teacher_name = models.CharField(max_length=128)
    contract_number = models.CharField(max_length=128)
    contract_date = models.CharField(max_length=128)
    function = models.CharField(max_length=128)
    teacher_passport = models.CharField(max_length=10)
    teacher_phone = models.CharField(max_length=48)
    teacher_address = models.CharField(max_length=128)
    employment_history_number = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    education = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    salary = models.CharField(max_length=128)




