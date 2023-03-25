from .models import Employee
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password


class UpgradedUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Hasła nie są takie same',
    }

    is_superuser = forms.BooleanField(
        label='Uprawnienia Admina',
        required=False,
        help_text='Zaznacz, jeżeli user ma być adminem.',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        validate_password(password1)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean(self):
        super().clean()
        is_superuser = self.cleaned_data.get('is_superuser')
        if is_superuser and not self.instance.is_superuser:
            self.fields['is_superuser'].help_text = 'Zaznacz, jeżeli user ma być adminem'
        return self.cleaned_data

    class Meta:
        model = Employee
        fields = ('username', 'name', 'surname', 'email', 'password1', 'password2', 'salon', 'is_superuser')
        labels = {
            'username': 'Nazwa użytkownika',
            'name': 'Imię',
            'surname': 'Nazwisko',
            'email': 'E-mail',
            'password1': 'Hasło',
            'password2': 'Potwórz hasło',
            'salon': 'Przypisz salon',
            'is_superuser': 'Uprawnienia Admina'
        }


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('username', 'name', 'surname', 'email', 'salon', 'is_superuser')
        labels = {
            'username': 'Nazwa użytkownika',
            'name': 'Imię',
            'surname': 'Nazwisko',
            'email': 'E-mail',
            'salon': 'Przypisz salon',
            'is_superuser': 'Uprawnienia Admina'
        }