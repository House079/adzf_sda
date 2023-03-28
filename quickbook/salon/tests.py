from django.test import TestCase
from .models import Salon


class SalonModelTest(TestCase):

    def setUp(self):
        Salon.objects.create(
            name='Example Salon',
            city='Łódź',
            address='Piotrkowska 34',
            details='This is an example salon.'
        )

    def test_salon_creation(self):
        salon = Salon.objects.get(name='Example Salon')
        self.assertEqual(salon.city, 'Łódź')
        self.assertEqual(salon.address, 'Piotrkowska 34')
        self.assertEqual(salon.details, 'This is an example salon.')

    def test_salon_string_representation(self):
        salon = Salon.objects.get(name='Example Salon')
        self.assertEqual(str(salon), 'Example Salon')

    def test_salon_name_max_length(self):
        salon = Salon.objects.get(name='Example Salon')
        max_length = salon._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_salon_city_max_length(self):
        salon = Salon.objects.get(name='Example Salon')
        max_length = salon._meta.get_field('city').max_length
        self.assertEqual(max_length, 30)

    def test_salon_address_max_length(self):
        salon = Salon.objects.get(name='Example Salon')
        max_length = salon._meta.get_field('address').max_length
        self.assertEqual(max_length, 255)