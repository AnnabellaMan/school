from django.contrib import admin
from .models import *


class StudentAdmin (admin.ModelAdmin):
    list_display = ["student_name", "parent_name", "parent_passport", "student_passport", "student_SNILS",
                    "parent_phone", "student_address", "class_number", "form_master"]
    search_fields = ["student_name"]


admin.site.register(Student, StudentAdmin)


