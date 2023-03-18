from django.db import models
from datetime import datetime


class EventType(models.Model):
    for_client = models.BooleanField(default=True)
    for_all = models.BooleanField(default=True)
    event_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    # client = ForClientManager()





