from django import forms
from django.forms import ModelForm
from . import models as management_models
from user import models as user_models
from user.constants import *


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
    state = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                              choices=States, initial='MP')

    class Meta:
        model = management_models.Hospitals
        fields = '__all__'


class AddDetails(ModelForm):
    first_name = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter your First Name.'
    })), required=True)
    last_name = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter your Last Name.'
    })), required=True)
    email = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'email',
        'placeholder': 'Enter your email.'
    })), required=False)
    phone = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter your Phone Number.'
    })), required=False)
    city = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter your city.'
    })), required=False)
    blood_group = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter Blood Group.'
    })), required=False)
    specify_other = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Specify Other.'
    })), required=False)
    additional_details = forms.CharField(widget=(forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 7,
        'placeholder': 'Please add additional details here.'
    })), required=False)
    state = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                              choices=States, initial='MP')

    class Meta:
        model = user_models.User
        fields = '__all__'
