from rest_framework import serializers
from .models import Patient, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    is_active = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        fields = '__all__'
    
    def create(self, validated_data):
        address = Address.objects.create(**validated_data.pop('address'))
        validated_data['address_id'] = address.id
        return super().create(validated_data)