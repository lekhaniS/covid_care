from django import forms
from django.forms import ModelForm
from . import models as management_models


class AddHospital(ModelForm):
    contact_info = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number',
        'placeholder': 'Enter your Contact Details.'
    })), required=True)
    hospital_name = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter Hospital Name.'
    })), required=True)
    city = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter City.'
    })), required=True)
    total_beds = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control custom_checkbox',
        'type': 'number',
        'placeholder': 'Number of beds'
    })), required=True)

    class Meta:
        model = management_models.Hospitals
        fields = '__all__'
