from django.db import models
from core.models import ModelBase
from patient.models import Patient

class Exam(ModelBase):
    doctor_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    patient_weight = models.FloatField()
    patient_height = models.FloatField()
    patient = models.OneToOneField(Patient, on_delete=models.DO_NOTHING, related_name="exam")
    