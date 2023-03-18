
from django import forms
from .models import EventType


class EventTypeForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = ('for_client', 'for_all', 'event_name', 'price', 'duration')