from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms as management_forms
from user import models as user_model


def home(request):
    return render(request, 'frontend/index.html', )


def WantHelp(request):
    context = {}
    context.update({'forms': management_forms.AddDetails})
    if request.method == 'POST':
        forms = management_forms.AddDetails(request.POST)
        if forms.is_valid():
            forms.save()
            context.update({'forms': management_forms.AddDetails,  'success': 'true'})
            return render(request, 'frontend/want_help.html', context)
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
            context.update({'forms': form, 'success': 'true'})
            return render(request, 'frontend/add_hospital.html', context)
        else:
            context.update({'errors': forms.errors, 'forms': forms})
    return render(request, 'frontend/add_hospital.html', context)


def medical_list(request):
    context = {}
    all_list = user_model.User.objects.all()
    context.update({'lists': all_list})
    return render(request, 'frontend/medical_list.html', context)


def user_filter(request):
    if request.method == 'POST':
        context = {}
        lists = None
        select_option1 = request.POST.get('select_option1')
        if int(select_option1) == 1:
            lists = user_model.User.objects.filter(oxygen_cylinder_supplier=True)
        if int(select_option1) == 2:
            lists = user_model.User.objects.filter(plasma_donor=True, blood_group=request.POST.get('blood_group'))
        context.update({'lists': lists})
        return render(request, 'frontend/medical_list.html', context)
    else:
        return redirect('frontend:medical_list')
