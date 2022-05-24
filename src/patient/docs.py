from django.utils.translation import gettext_lazy as _
from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework import status
from . import serializers

class PatientAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys):
        return ['Patient routes']


patient_create_docs = {
    "auto_schema": PatientAutoSchema,
    "operation_summary": _('Create patient'),
    "responses": {status.HTTP_201_CREATED: serializers.PatientSerializer},
}

patient_retrieve_docs = {
    "auto_schema": PatientAutoSchema,
    "operation_summary": _('Get patient details'),
    "responses": {status.HTTP_200_OK: serializers.PatientSerializer},
}

patient_list_docs = {
    "auto_schema": PatientAutoSchema,
    "operation_summary": _('List patients'),
    "responses": {status.HTTP_200_OK: serializers.PatientSerializer},
}

patient_update_docs = {
    "auto_schema": PatientAutoSchema,
    "operation_summary": _('Update patient'),
    "responses": {status.HTTP_200_OK: serializers.PatientSerializer},
}

patient_partial_update_docs = {
    "auto_schema": PatientAutoSchema,
    "operation_summary": _('Update patient'),
    "responses": {status.HTTP_200_OK: serializers.PatientSerializer},
}

patient_destroy_docs = {
    "auto_schema": PatientAutoSchema,
    "operation_summary": _('Delete patient'),
    "responses": {status.HTTP_204_NO_CONTENT: ''},
}