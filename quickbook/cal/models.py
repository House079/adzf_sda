import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse
from salon.models import Salon
from users.models import CustomUser


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    day = models.DateField('Day of the appointment')
    start_time = models.TimeField('Start time')
    end_time = models.TimeField('End time')
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name="events_salon")
    employee = models.ForeignKey(CustomUser, on_delete=SET_NULL, null=True, related_name="events_employee")


    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  # edge case
            overlap = False
        elif (fixed_start <= new_start <= fixed_end) or (
                fixed_start <= new_end <= fixed_end):  # inner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  # outer limits
            overlap = True

        return overlap

    def check_employee_availability(self, employee, salon):
        # TODO: add employee availability verification
        pass

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(f'There is an overlap with another event: {event.day}, {event.start_time} - {event.end_time}')

                # if self.check_employee_availability is False:
                #     raise ValidationError('This employee is not available at this period of time')
                # TODO add employee availability check


