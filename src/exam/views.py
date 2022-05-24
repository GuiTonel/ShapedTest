from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from core.paginations import DefaultLimitPagination
from .models import Exam
from .serializers import ExamSerializer
from . import docs, serializers


@method_decorator(name="create", decorator=swagger_auto_schema(**docs.exam_create_docs))
@method_decorator(name="retrieve", decorator=swagger_auto_schema(**docs.exam_retrieve_docs))
@method_decorator(name="list", decorator=swagger_auto_schema(**docs.exam_list_docs))
@method_decorator(name="destroy", decorator=swagger_auto_schema(**docs.exam_destroy_docs))
@method_decorator(name="update", decorator=swagger_auto_schema(**docs.exam_update_docs))
@method_decorator(name="partial_update", decorator=swagger_auto_schema(**docs.exam_partial_update_docs))
class ExamView(ModelViewSet):
    queryset = Exam.objects.all().filter(is_active = True).select_related('patient').order_by('-created_at')
    serializer_class = ExamSerializer
    serializer_classes = {
        'create': serializers.ExamCreateSerializer,
        'update': serializers.ExamCreateSerializer,
        'partial_update': serializers.ExamCreateSerializer,
    }
    default_serializer_class = ExamSerializer 
    permission_classes = ()
    pagination_class = DefaultLimitPagination
    ordering_fields = ('created_at', 'patient__age', 'doctor_name',)
    search_fields = ('doctor_name', 'patient__name')
    filterset_fields = {
        'date': ['exact', 'lte', 'gte'], 
        'patient_weight': ['exact', 'lte', 'gte'], 
        'patient_height': ['exact', 'lte', 'gte'], 
        'patient__age': ['exact', 'lte', 'gte'],
        }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def destroy(self, request, *args, **kwargs):
        Exam.objects.filter(**kwargs).update(is_active=False)
        return Response({'sucess': True}, status=status.HTTP_204_NO_CONTENT)