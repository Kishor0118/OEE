from django.test import TestCase
from .models import Machines, ProductionLog
from rest_framework.test import APIClient

class MachineTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.machine = Machines.objects.create(machine_name="Machine 1", machine_serial_no="SN12345")

    def test_machine_creation(self):
        self.assertEqual(self.machine.machine_name, "Machine 1")
        self.assertEqual(self.machine.machine_serial_no, "SN12345")

    def test_get_machines(self):
        response = self.client.get('/api/machines/')
        self.assertEqual(response.status_code, 200)

class ProductionLogTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.machine = Machines.objects.create(machine_name="Machine 1", machine_serial_no="SN12345")
        self.production_log = ProductionLog.objects.create(cycle_no="CN001", unique_id="UID001",
                                                           material_name="Material 1", machine=self.machine,
                                                           start_time="2023-01-01T00:00:00Z", end_time="2023-01-01T01:00:00Z",
                                                           duration=1.0)

    def test_production_log_creation(self):
        self.assertEqual(self.production_log.cycle_no, "CN001")
        self.assertEqual(self.production_log.unique_id, "UID001")

    def test_get_production_logs(self):
        response = self.client.get('/api/productionlogs/')
        self.assertEqual(response.status_code, 200)
