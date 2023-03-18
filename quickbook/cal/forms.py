from django.forms import ModelForm, DateInput
from django import forms
from .models import Event
from salon.models import Salon
from users.models import CustomUser

class EventForm(ModelForm):
  salon = forms.ModelChoiceField(queryset=Salon.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
  employee = forms.ModelChoiceField(queryset=CustomUser.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))
  class Meta:
    model = Event
    fields = ['title', 'description', 'day', 'start_time', 'end_time', 'salon', 'employee']
    widgets = {
      'day': forms.DateInput(attrs={'type': 'date'}),
      'start_time': forms.TimeInput(attrs={'type': 'time'}),
      'end_time': forms.TimeInput(attrs={'type': 'time'}),
    }