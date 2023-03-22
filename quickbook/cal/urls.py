from django.urls import path
from . import views


app_name = 'cal'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<event_id>/', views.event, name='event_edit'),
    path('get_employees/', views.get_employees, name='get_employees'),
    path('detail/<int:pk>', views.EventDetail.as_view(), name='detail'),
    path('list/', views.EventList.as_view(), name='list'),
    path('delete/<int:pk>', views.EventDelete.as_view(), name='delete'),
    path('create/<int:pk>', views.EventCreate.as_view(), name='create'),
]