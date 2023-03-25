from django.db import models
from datetime import datetime, timedelta


class EventType(models.Model):
    # TIME_CHOOSE = (enumerate(['15 min', '30 min', '1 godzina', '2 godziny', '4 godziny']))
    event_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField(default=timedelta(minutes=0, hours=0))







