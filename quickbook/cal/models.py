import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse
from salon.models import Salon
from users.models import Employee


class Event(models.Model):
    title = models.CharField('Tytuł', max_length=200)
    description = models.TextField('Opis')
    day = models.DateField('Dzień')
    start_time = models.TimeField('Początek')
    end_time = models.TimeField('Koniec')
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=SET_NULL, null=True)

    @property
    def get_url(self):
        return reverse('cal:event_edit', args=(self.id,))

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:
            overlap = False
        elif (fixed_start <= new_start <= fixed_end) or (
                fixed_start <= new_end <= fixed_end):
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:
            overlap = True

        return overlap

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Czas zakończenia musi być po czasie rozpoczęcia.')

        events = Event.objects.filter(day=self.day, employee=self.employee)

        for event in events:
            if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                raise ValidationError(
                    f'Pracownik {self.employee} nie jest dostępny w tym czasie: {event.day}, {event.start_time} - {event.end_time}')
