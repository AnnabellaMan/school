from django.contrib import admin
from .models import *


class TimetableAdmin (admin.ModelAdmin):
    list_display = ["class_number", "classroom", "teacher", "day_of_the_week", "lesson_number", "subject"]
    search_fields = ["class", "teacher", "day_of_the_week"]


admin.site.register(Timetable, TimetableAdmin)


