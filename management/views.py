from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms as management_forms
from user import models as user_model
from . import models as management_models

from django.db.models import Q

# from .cron import news_api_data_storage


def home(request):
    return render(request, 'frontend/index.html', )


def WantHelp(request):
    context = {}
    context.update({'forms': management_forms.AddDetails})
    if request.method == 'POST':
        forms = management_forms.AddDetails(request.POST)
        if forms.is_valid():
            forms.save()
            context.update({'forms': management_forms.AddDetails, 'success': 'true'})
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
        print(forms)
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
        if int(select_option1) == 0:
            lists = user_model.User.objects.filter(oxygen_cylinder_supplier=True)
        if int(select_option1) == 1:
            lists = user_model.User.objects.filter(plasma_donor=True, blood_group=request.POST.get('blood_group'))
        if int(select_option1) == 2:
            lists = user_model.User.objects.filter(medical_supplier=True)
        if int(select_option1) == 3:
            lists = user_model.User.objects.filter(medical_support=True)
        context.update({'lists': lists})
        return render(request, 'frontend/medical_list.html', context)
    else:
        return redirect('frontend:medical_list')

def filter_list(request, pk):
    context = {}
    if pk is not None:
        if int(pk) == 3:
            lists = user_model.User.objects.filter(medical_support=True)
            context.update({'lists': lists, 'key': 3})
        elif int(pk) == 2:
            lists = user_model.User.objects.filter(medical_supplier=True)
            context.update({'lists': lists, 'key': 2})
        elif int(pk) == 0:
            lists = user_model.User.objects.filter(oxygen_cylinder_supplier=True)
            context.update({'lists': lists, 'key': 0})
        elif int(pk) == 1:
            lists = user_model.User.objects.filter(plasma_donor=True)
            context.update({'lists': lists, 'key': 1})
        elif int(pk) == 4:
            lists = management_models.Hospitals.objects.all()
            print(pk, lists)
            context.update({'lists': lists, 'key': 4})
        return render(request, 'frontend/medical_list.html', context)
    return redirect('frontend:medical_list')


def blood_group(request, pk):
    context = {}
    if pk is not None:
        lists = user_model.User.objects.filter(plasma_donor=True, blood_group=str(pk)).exclude(blood_group='')
        context.update({'lists': lists, 'key': 1, 'plasma_key': str(pk)})
        return render(request, 'frontend/medical_list.html', context)
    return redirect('frontend:medical_list')


def about_us(request):
    return render(request, 'frontend/about.html')


def get_news():
    return management_models.Article.objects.all().exclude(urlToImage=None)


def latest_news(request):
    # news_api_data_storage()
    news = get_news()
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'frontend/latest_news.html', {'articles': page_obj})
