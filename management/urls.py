from django.urls import path

from . import views
app_name = 'frontend'
urlpatterns = [
    path('', views.home, name='index'),
    path('help/', views.WantHelp, name='want_help'),
    path('add/hospital/', views.add_hospital, name='add_hospital'),
]
