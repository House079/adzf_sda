from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'salon'

urlpatterns = [
    path('', views.SalonList.as_view(), name='list'),
    path('add', views.send_salon, name='send_salon'),
    path('detail/<int:pk>', views.SalonDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.SalonUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.SalonDelete.as_view(), name='delete'),
]
