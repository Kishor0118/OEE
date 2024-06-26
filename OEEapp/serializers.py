from rest_framework import serializers
from .models import Machines, ProductionLog

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machines
        fields = '__all__'

class ProductionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLog
        fields = '__all__'
