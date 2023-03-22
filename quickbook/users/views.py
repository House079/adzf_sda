from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DeleteView, UpdateView
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


class EmployeesList(ListView):
    model = Employee
    template_name = 'users/employees.html'
    fields = ('name', 'surname', 'email', 'date_joined')


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('users:employees_list')


class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'users/employee_update_form.html'
    fields = ('username', 'name', 'surname', 'email', 'salon')
    success_url = reverse_lazy('users:employees_list')


