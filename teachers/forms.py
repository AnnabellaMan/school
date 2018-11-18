from django import forms
from .models import *


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        exclude = [""]
