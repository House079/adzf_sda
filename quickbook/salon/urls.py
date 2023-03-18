from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'salon'

urlpatterns = [
    path('', views.send_salon, name='send_salon'),
    path('update/<int:pk>', views.SalonUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.SalonDelete.as_view(), name='delete'),
]
