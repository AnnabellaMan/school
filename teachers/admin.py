from django.contrib import admin
from .models import *


class TeacherAdmin (admin.ModelAdmin):
    list_display = ["teacher_name", "teacher_passport", "teacher_phone", "teacher_address", "subject",
                    "education", "category", "classroom", "mastering", "salary"]
    search_fields = ["teacher_name"]


admin.site.register(Teacher, TeacherAdmin)


