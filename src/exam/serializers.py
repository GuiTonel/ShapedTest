from rest_framework import serializers
from patient.serializers import PatientSerializer
from .models import Exam

class ExamSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Exam
        fields = '__all__'

class ExamCreateSerializer(serializers.ModelSerializer):
    is_active = serializers.ReadOnlyField()

    class Meta:
        model = Exam
        fields = '__all__'