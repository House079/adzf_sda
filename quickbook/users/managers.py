from django.contrib.auth.base_user import BaseUserManager


class EmployeeManager(BaseUserManager):
    def create_user(self, email, username, name, surname, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, name=name, surname=surname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, surname, password=None):
        user = self.create_user(email, username, name, surname, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
