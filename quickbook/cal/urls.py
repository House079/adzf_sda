from django.urls import path
from . import views

app_name = 'cal'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<event_id>/', views.event, name='event_edit'),
    path('get_employees/', views.get_employees, name='get_employees')
]