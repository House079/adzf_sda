from django import forms
from .models import EventType
from datetime import timedelta


class DurationInput(forms.TextInput):
    input_type = 'time'

    def __init__(self, attrs=None):
        attrs = attrs or {}
        attrs['step'] = 60
        super().__init__(attrs)

    def format_value(self, value):
        if isinstance(value, timedelta):
            hours = int(value.total_seconds() // 3600)
            minutes = int((value.total_seconds() % 3600) // 60)
            return f'{hours:02d}:{minutes:02d}'
        return super().format_value(value)

    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        if value:
            try:
                hours, minutes = map(int, value.split(':')[:2])
                value = timedelta(hours=hours, minutes=minutes)
            except (ValueError, TypeError):
                pass
        return value


class EventTypeForm(forms.ModelForm):
    duration = forms.DurationField(widget=DurationInput, label='Czas trwania (hh:mm)')

    class Meta:
        model = EventType
        fields = ('event_name', 'price', 'duration')
        labels = {
            'event_name': 'Nazwa usługi',
            'price': 'Cena',
        }

    def clean_duration(self):
        duration = self.cleaned_data['duration']
        if isinstance(duration, str):
            hours, minutes = map(int, duration.split(':'))
            duration = timedelta(hours=hours, minutes=minutes)
        else:
            duration_in_seconds = duration.total_seconds()
            duration = timedelta(seconds=duration_in_seconds)
        return duration


class EventTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = ('event_name', 'price', 'duration')
        labels = {
            'event_name': 'Nazwa usługi',
            'price': 'Cena',
            'duration': 'Czas trwania (hh:mm)',
        }
# class EventTypeForm(forms.ModelForm):
#     class Meta:
#         model = EventType
#         fields = ('event_name', 'price', 'duration')
#         labels = {
#             'event_name': 'Nazwa usługi',
#             'price': 'Cena',
# #             'duration': 'Czas trwania (hh:mm:ss)',
#         }
