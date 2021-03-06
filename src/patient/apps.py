from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class PatientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patient'
    verbose_name = _('Patient')