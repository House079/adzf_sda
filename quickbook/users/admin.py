from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'name', 'email', 'salon', 'date_joined', 'is_staff', 'is_superuser')
