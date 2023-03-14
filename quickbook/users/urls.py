from django.urls import path
from .views import user, remove_user, remove_users_be
urlpatterns = [
    path(' ', user, name='user'),

    path('register/', user, name='register'),
    path('remove/', remove_user, name='remove'),
    path('remove_users_be/', remove_users_be, name='remove'),
]

