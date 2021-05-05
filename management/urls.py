from django.urls import path

from . import views
app_name = 'frontend'
urlpatterns = [
    path('', views.home, name='index'),
    path('help/', views.WantHelp, name='want_help'),
    path('add/hospital/', views.add_hospital, name='add_hospital'),
    path('list/', views.medical_list, name='medical_list'),
    path('filter/', views.user_filter, name='user_filter'),
    path('news/', views.news_view, name='news'),
    path('filter-list/<str:pk>', views.filter_list, name='filter_list'),
    path('plasma/<str:pk>', views.blood_group, name='plasma'),
]
