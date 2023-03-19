from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UpgradedUserCreationForm


class SignUp(CreateView):
    form_class = UpgradedUserCreationForm
    success_url = reverse_lazy('users:register')
    template_name = 'users/signup.html'


class UserPanel(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_panel.html'
