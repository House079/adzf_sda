from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CATEGORIS


class UserRegisterForm(UserCreationForm):
    """Budujemy nad podstawową formą co chcemy dodac GOOGLE"""

    first_name = forms.CharField(max_length=30, help_text="first name")
    last_name = forms.CharField(max_length=30, help_text="last name")
    website = forms.CharField(max_length=256)
    position = forms.CharField(max_length=256, widget=forms.Select(choices=CATEGORIS))

    """ Dodanie 4 pola do formy tworzenia urzytkownika"""

    class Meta:

        model = User
        fields = ["username", "first_name", "last_name", "website", "position", "password1", "password2"]

    def __init__(self, *args, **kwargs):

        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Enter your username"
        # self.fields["username"].label = "Case sensitive"
        # self.fields["username"].help_text = "Username"
        self.fields["first_name"].widget.attrs["placeholder"] = "Please enter first name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Enter last name"
        self.fields["website"].widget.attrs["placeholder"] = "Enter website"
        self.fields["position"].widget.attrs["placeholder"] = "Select position"
        self.fields["password1"].widget.attrs["placeholder"] = ""
        self.fields["password2"].widget.attrs["placeholder"] = ""

        """Atrybuty do pol html wyswietla co ma byc uzupełnione"""