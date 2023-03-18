from django.forms import ModelForm, DateInput
from django import forms
from .models import Event
from salon.models import Salon
from users.models import Employee


class EventForm(forms.ModelForm):
  salon = forms.ModelChoiceField(queryset=Salon.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
  employee = forms.ModelChoiceField(queryset=Employee.objects.none(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))

  class Meta:
    model = Event
    fields = ['title', 'description', 'day', 'start_time', 'end_time', 'salon', 'employee']
    widgets = {
      'day': forms.DateInput(attrs={'type': 'date'}),
      'start_time': forms.TimeInput(attrs={'type': 'time'}),
      'end_time': forms.TimeInput(attrs={'type': 'time'}),
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['employee'].queryset = Employee.objects.none()

    if not self.instance.pk and 'salon' in self.data:
      try:
        salon_id = int(self.data.get('salon'))
        self.fields['employee'].queryset = Employee.objects.filter(salon_id=salon_id).order_by('name')
      except (ValueError, TypeError):
        pass
    elif self.instance.pk:
      self.fields['employee'].queryset = self.instance.salon.employees.order_by('name')




