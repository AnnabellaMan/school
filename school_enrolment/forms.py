from django import forms
from .models import *


class SchoolEnrolmentForm(forms.ModelForm):

    class Meta:
        model = SchoolEnrolment
        exclude = [""]
