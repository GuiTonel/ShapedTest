from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import ModelBase


class Address(models.Model):
    street = models.CharField(verbose_name=_("Street name"), max_length=255)
    number = models.PositiveIntegerField(verbose_name=_("House number"))
    city = models.CharField(verbose_name=_("City name"), max_length=100)
    state = models.CharField(verbose_name=_("State name"), max_length=100)
    country = models.CharField(verbose_name=_("Country name"), max_length=100)    


class Patient(ModelBase):
    name = models.CharField(verbose_name=_("Patient name"), max_length=50)
    age = models.PositiveSmallIntegerField(verbose_name=_('Patient age'), default=0)
    address = models.OneToOneField(Address, on_delete=models.PROTECT, related_name="patient", verbose_name=_("Patient address"))