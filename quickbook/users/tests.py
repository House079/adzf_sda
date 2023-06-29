from django.test import TestCase
from .models import Employee, Salon

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.salon = Salon.objects.create(name='Test Salon')
        self.employee = Employee.objects.create(
            email='testemployee@test.com',
            username='testemployee',
            name='Test',
            surname='Employee',
            salon=self.salon,
        )

    def test_employee_creation(self):
        employee = self.employee
        self.assertTrue(isinstance(employee, Employee))
        self.assertEqual(employee.__str__(), employee.username)
        self.assertEqual(employee.get_full_name(), 'Test Employee')
        self.assertEqual(employee.get_short_name(), 'Test')
        self.assertEqual(employee.is_active, True)
        self.assertEqual(employee.is_superuser, False)
        self.assertEqual(employee.is_staff, True)
        self.assertEqual(employee.salon, self.salon)