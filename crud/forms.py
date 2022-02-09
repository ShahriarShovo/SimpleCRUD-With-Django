from django import forms
from crud.models import Employee_info

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee_info
        fields="__all__"