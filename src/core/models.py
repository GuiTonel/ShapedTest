from django.db import models
from django.utils.translation import gettext_lazy as _

class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True