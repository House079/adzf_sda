from datetime import datetime
from django.db import models
from salon.models import Salon
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.managers import EmployeeManager


class Employee(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(
        default=datetime.now, blank=True)  # To add then run migrations
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='employees', null=True)

    objects = EmployeeManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'surname']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_short_name(self):
        return self.name

