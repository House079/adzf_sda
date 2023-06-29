from django.test import TestCase
from datetime import date, time
from users.models import Salon, Employee
from cal.models import Event


class EventTestCase(TestCase):

    def setUp(self):
        self.salon = Salon.objects.create(name='Test Salon')
        self.employee = Employee.objects.create(name='Test Employee')

        self.event = Event.objects.create(
            title='Test Event',
            description='This is a test event',
            day=date.today(),
            start_time=time(9, 0),
            end_time=time(11, 0),
            salon=self.salon,
            employee=self.employee
        )

    def test_event_title(self):
        self.assertEqual(self.event.title, 'Test Event')

    def test_event_description(self):
        self.assertEqual(self.event.description, 'This is a test event')

    def test_event_day(self):
        self.assertEqual(self.event.day, date.today())

    def test_event_start_time(self):
        self.assertEqual(self.event.start_time, time(9, 0))

    def test_event_end_time(self):
        self.assertEqual(self.event.end_time, time(11, 0))

    def test_event_salon(self):
        self.assertEqual(self.event.salon, self.salon)

    def test_event_employee(self):
        self.assertEqual(self.event.employee, self.employee)

    def test_event_employee_null(self):
        event = Event.objects.create(
            title='Test Event 2',
            description='This is another test event',
            day=date.today(),
            start_time=time(9, 0),
            end_time=time(11, 0),
            salon=self.salon
        )
        self.assertIsNone(event.employee)