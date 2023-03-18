from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'day', 'start_time', 'end_time', 'salon', 'employee']