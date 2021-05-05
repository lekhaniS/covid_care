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
