from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import EventType


class EventTypeModelTestCase(TestCase):
    def setUp(self):
        self.event_type = EventType.objects.create(
            event_name='Test event',
            price=100.00,
            duration=timedelta(hours=1)
        )

    def test_event_type_creation(self):
        self.assertTrue(isinstance(self.event_type, EventType))
        self.assertEqual(self.event_type.__str__(), f'{self.event_type.event_name} | {self.event_type.duration}')

    def test_event_type_price(self):
        self.assertEqual(self.event_type.price, 100.00)

    def test_event_type_duration(self):
        self.assertEqual(self.event_type.duration, timedelta(hours=1))

    def test_event_type_default_duration(self):
        event_type = EventType.objects.create(
            event_name='Test event without duration',
            price=50.00
        )
        self.assertEqual(event_type.duration, timedelta(minutes=0, hours=0))

    def test_event_type_update(self):
        new_price = 150.00
        self.event_type.price = new_price
        self.event_type.save()
        updated_event_type = EventType.objects.get(id=self.event_type.id)
        self.assertEqual(updated_event_type.price, new_price)

    def test_event_type_delete(self):
        event_type_id = self.event_type.id
        self.event_type.delete()
        with self.assertRaises(EventType.DoesNotExist):
            EventType.objects.get(id=event_type_id)
