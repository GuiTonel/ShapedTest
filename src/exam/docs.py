from django.utils.translation import gettext_lazy as _
from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework import status
from . import serializers

class ExamAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys):
        return ['Exam routes']


exam_create_docs = {
    "auto_schema": ExamAutoSchema,
    "operation_summary": _('Create exam'),
    "responses": {status.HTTP_201_CREATED: serializers.ExamCreateSerializer},
}

exam_retrieve_docs = {
    "auto_schema": ExamAutoSchema,
    "operation_summary": _('Get exam details'),
    "responses": {status.HTTP_200_OK: serializers.ExamSerializer},
}

exam_list_docs = {
    "auto_schema": ExamAutoSchema,
    "operation_summary": _('List exams'),
    "responses": {status.HTTP_200_OK: serializers.ExamSerializer},
}

exam_update_docs = {
    "auto_schema": ExamAutoSchema,
    "operation_summary": _('Update exam'),
    "responses": {status.HTTP_200_OK: serializers.ExamSerializer},
}

exam_partial_update_docs = {
    "auto_schema": ExamAutoSchema,
    "operation_summary": _('Update exam'),
    "responses": {status.HTTP_200_OK: serializers.ExamSerializer},
}

exam_destroy_docs = {
    "auto_schema": ExamAutoSchema,
    "operation_summary": _('Delete exam'),
    "responses": {status.HTTP_204_NO_CONTENT: ''},
}