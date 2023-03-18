from django.forms import ModelForm, DateInput
from django import forms
from .models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = ['title', 'day', 'description', 'start_time', 'end_time']
    widgets = {
      'day': forms.DateInput(attrs={'type': 'date'}),
      'start_time': forms.TimeInput(attrs={'type': 'time'}),
      'end_time': forms.TimeInput(attrs={'type': 'time'}),
    }