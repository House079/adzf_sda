from django import forms
from .models import Salon


class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ('name', 'city', 'city', 'address', 'opening_hours')
