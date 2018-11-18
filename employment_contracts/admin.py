from django.contrib import admin
from .models import *


class EmploymentContractAdmin (admin.ModelAdmin):
    list_display = ["teacher_name", "contract_number", "contract_date", "function", "teacher_passport",
                    "teacher_phone", "teacher_address", "subject", "employment_history_number",
                    "education", "category", "salary"]
    search_fields = ["teacher_name"]


admin.site.register(EmploymentContract, EmploymentContractAdmin)


