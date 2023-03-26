from django.urls import path
from . import views

app_name = 'prices'

urlpatterns = [
    path('', views.EventTypesList.as_view(), name='prices'),
    path('create/', views.CreateEvent.as_view(), name='create'),
    path('', views.send_event, name='send_event'),
    path('delete/<int:pk>', views.EventTypeDelete.as_view(), name='delete'),
    path('update/<int:pk>', views.EventTypeUpdate.as_view(), name='update'),

]