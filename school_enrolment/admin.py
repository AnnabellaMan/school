from django.contrib import admin
from .models import *


class SchoolEnrolmentAdmin (admin.ModelAdmin):
    list_display = ["student_name", "parent_name", "contract_number", "contract_date", "parent_passport",
                    "student_passport", "student_SNILS", "parent_phone", "student_address"]
    search_fields = ["student_name"]


admin.site.register(SchoolEnrolment, SchoolEnrolmentAdmin)


