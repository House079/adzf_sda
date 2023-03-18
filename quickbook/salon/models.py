# import jsonfield
from django.db import models
import datetime


# Create your models here.
def default_opening_hours():
    return {'monday': {'open': '08:00', 'close': '18:00'},
            'tuesday': {'open': '08:00', 'close': '18:00'},
            'wednesday': {'open': '08:00', 'close': '18:00'},
            'thursday': {'open': '08:00', 'close': '18:00'},
            'friday': {'open': '08:00', 'close': '18:00'},
            'sunday': {'open': '08:00', 'close': '18:00'},
            }


class Salon(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    opening_hours = models.JSONField('Opening hours', default=default_opening_hours())
