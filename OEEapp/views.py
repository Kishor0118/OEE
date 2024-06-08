from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Machines, ProductionLog
from .serializers import MachineSerializer, ProductionLogSerializer


class ProductionLogViewSet(viewsets.ModelViewSet):
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machines.objects.all()
    serializer_class = MachineSerializer

    @action(detail=True, methods=['get'])
    def calculate_oee(self, request, pk=None):
        machine = self.get_object()
        logs = ProductionLog.objects.filter(machine=machine)
        
        # Calculate OEE
        available_time = 3 * 8  # 3 shifts, 8 hours each
        ideal_cycle_time = 5  # Ideal cycle time in minutes

        good_products = 0
        total_products = 0
        total_duration = 0

        for log in logs:
            cycle_time = (log.end_time - log.start_time).total_seconds() / 60  # Convert to minutes
            total_products += 1
            total_duration += cycle_time
            if cycle_time == ideal_cycle_time:
                good_products += 1

        actual_output = total_products
        available_operating_time = total_products * ideal_cycle_time
        unplanned_downtime = available_time - (total_duration / 60)  # Convert duration to hours

        availability = (available_time - unplanned_downtime) / available_time * 100
        performance = (ideal_cycle_time * actual_output) / total_duration * 100
        quality = good_products / total_products * 100

        oee = (availability * performance * quality) / 10000

        return Response({
            'availability': availability,
            'performance': performance,
            'quality': quality,
            'oee': oee
        })
