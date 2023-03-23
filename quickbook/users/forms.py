from .models import Employee
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class UpgradedUserCreationForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = ('username', 'name', 'surname', 'email', 'password1', 'password2', 'salon', 'is_superuser')
    # OPTIONS = [
    #     ('option1', 'Option 1'),
    #     ('option2', 'Option 2'),
    #     ('option3', 'Option 3'),
    # ]
    # salon = forms.ChoiceField(label='Salon', choices=OPTIONS)


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data