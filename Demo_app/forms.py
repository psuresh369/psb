from django import forms
from .models import Create
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Create
        fields = ['name',]
