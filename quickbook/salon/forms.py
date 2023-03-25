from django import forms
from .models import Salon


class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ('name', 'city', 'address', 'details')
        labels = {
            'name': 'Nazwa',
            'city': 'Miasto',
            'address': 'Adres',
            'details': 'Szczegóły'
        }

