from django import forms
from .models import UserInformation

class UserInformationForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = ['name', 'age', 'email', 'phone', 'address', 'country', 'state', 'gender', 'occupation', 'comments']

        widgets = {
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]),
            'occupation': forms.Select(choices=[('Student', 'Student'), ('Employee', 'Employee'), ('Other', 'Other')]),
        }
