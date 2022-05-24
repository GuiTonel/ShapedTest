from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from core.paginations import DefaultLimitPagination
from .models import Patient
from .serializers import PatientSerializer
from . import docs


@method_decorator(name="create", decorator=swagger_auto_schema(**docs.patient_create_docs))
@method_decorator(name="retrieve", decorator=swagger_auto_schema(**docs.patient_retrieve_docs))
@method_decorator(name="list", decorator=swagger_auto_schema(**docs.patient_list_docs))
@method_decorator(name="destroy", decorator=swagger_auto_schema(**docs.patient_destroy_docs))
@method_decorator(name="update", decorator=swagger_auto_schema(**docs.patient_update_docs))
@method_decorator(name="partial_update", decorator=swagger_auto_schema(**docs.patient_partial_update_docs))
class PatientView(ModelViewSet):
    queryset = Patient.objects.all().filter(is_active = True).select_related('address').order_by('-created_at')
    serializer_class = PatientSerializer
    permission_classes = ()
    pagination_class = DefaultLimitPagination
    ordering_fields = ('created_at', 'age',)
    search_fields = ('name', 'address__city', 'address__state', 'address__street')
    filterset_fields = {
        'name': ['exact'], 
        'address__city': ['exact'], 
        'address__state': ['exact'], 
        'address__street': ['exact'], 
        'age': ['exact', 'gte', 'lte'],
        }
    
    def destroy(self, request, *args, **kwargs):
        Patient.objects.filter(**kwargs).update(is_active=False)
        return Response({'sucess': True}, status=status.HTTP_204_NO_CONTENT)