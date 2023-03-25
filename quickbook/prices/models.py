from django.db import models
from datetime import datetime, timedelta


class EventType(models.Model):
    event_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField(default=timedelta(minutes=0, hours=0))

    def __str__(self):
        return f'{self.event_name} | {self.duration}'
