from django.db import models
from user.models import User
from user.constants import States


class Hospitals(models.Model):
    contact_info = models.CharField(max_length=20, null=False, blank=False)
    hospital_name = models.CharField(max_length=200)
    state = models.CharField(max_length=15, choices=States, default="MP")
    city = models.CharField(max_length=30, null=False, blank=False)
    total_beds = models.CharField(max_length=4, null=True, blank=True)
    oxygen_availability = models.BooleanField(default=False)
    ventilator_availability = models.BooleanField(default=False)


class Article(models.Model):
    source = models.CharField(max_length=150, null=True, blank=True)
    author = models.CharField(max_length=150, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    urlToImage = models.CharField(max_length=500, null=True, blank=True)
    publishedAt = models.CharField(max_length=150, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
