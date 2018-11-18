from django import forms
from .models import *


class EmploymentContractForm(forms.ModelForm):

    class Meta:
        model = EmploymentContract
        exclude = [""]
