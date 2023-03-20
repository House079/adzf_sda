from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from .models import Employee


class EmployeeBackend(ModelBackend):
    model = get_user_model()

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Employee.objects.get(username=username)
        except Employee.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return self.model.objects.get(pk=user_id)
        except self.model.DoesNotExist:
            return None