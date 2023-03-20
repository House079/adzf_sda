from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UpgradedUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView

from .models import Employee


class SignUp(CreateView):
    form_class = UpgradedUserCreationForm
    success_url = reverse_lazy('users:register')
    template_name = 'users/signup.html'


class UserPanel(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_panel.html'


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm
    success_url = reverse_lazy('/')

