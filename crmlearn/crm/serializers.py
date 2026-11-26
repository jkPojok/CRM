from rest_framework import serializers
from .models import Doctor
from .models import Patient
from .models import Appointment
from django.utils import timezone

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
            model = Patient
            fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
            model = Appointment
            fields = '__all__'

    