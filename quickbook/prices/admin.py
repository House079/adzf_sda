from django.contrib import admin

from .models import EventType

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'price', 'duration')
