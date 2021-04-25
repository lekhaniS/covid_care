from django.shortcuts import render
from django.http import HttpResponse
from . import forms as management_forms


def home(request):
    return render(request, 'frontend/index.html', )


def WantHelp(request):
    context = {}
    context.update({'forms': management_forms.AddDetails})
    if request.method == 'POST':
        forms = management_forms.AddDetails(request.POST)
        if forms.is_valid():
            forms.save()
        else:
            context.update({'errors': forms.errors, 'forms': forms})
            return render(request, 'frontend/want_help.html', context)
    return render(request, 'frontend/want_help.html', context)


def add_hospital(request):
    context = {}
    form = management_forms.AddHospital
    context.update({'forms': form})

    if request.method == 'POST':
        forms = management_forms.AddHospital(request.POST)
        if forms.is_valid():
            forms.save()
        else:
            context.update({'errors': forms.errors, 'forms': forms})
    return render(request, 'frontend/add_hospital.html', context)


def medical_list(request):
    return render(request, 'frontend/medical_list.html')
