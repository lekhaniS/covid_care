from django.db import models
from django.contrib.auth.models import AbstractUser
from user.constants import *


class User(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, unique=True, blank=False, null=False)
    state = models.CharField(max_length=15, choices=States, default="MP")
    city = models.CharField(max_length=255, blank=False, null=False)
    blood_group = models.CharField(max_length=3, choices=BloodGroup, blank=True, null=True)
    oxygen_cylinder_supplier = models.BooleanField(default=False)
    plasma_donor = models.BooleanField(default=False)
    medical_supplier = models.BooleanField(default=False)
    medical_support = models.BooleanField(default=False)
    doctor = models.BooleanField(default=False)
    health_care_worker = models.BooleanField(default=False)
    additional_details = models.CharField(max_length=1000, blank=True, null=True)
    remdisivr = models.BooleanField(default=False)
    toclizumab = models.BooleanField(default=False)
    specify_other = models.CharField(max_length=255, blank=True, null=True)
    REQUIRED_FIELDS = []

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email
