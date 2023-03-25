from django import forms
from .models import EventType


class EventTypeForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = ('event_name', 'price', 'duration')
        labels = {
            'event_name': 'Nazwa usługi',
            'price': 'Cena',
            'duration': 'Czas trwania (hh:mm:ss)',
        }
