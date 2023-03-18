from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UpgradedUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'password1', 'password2', 'salon')
    #
    # OPTIONS = [
    #     ('option1', 'Option 1'),
    #     ('option2', 'Option 2'),
    #     ('option3', 'Option 3'),
    # ]
    # salon = forms.ChoiceField(label='Salon', choices=OPTIONS)


