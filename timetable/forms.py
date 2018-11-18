from django import forms
from .models import *


class TimetableForm(forms.ModelForm):

    class Meta:
        model = Timetable
        exclude = [""]
