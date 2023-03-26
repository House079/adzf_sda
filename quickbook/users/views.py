from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UpgradedUserCreationForm, CustomAuthenticationForm, EmployeeUpdateForm, PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Employee
from salon.views import superuser_required, staff_user_required


class SignUp(PermissionRequiredMixin, CreateView):
    form_class = UpgradedUserCreationForm
    success_url = reverse_lazy('users:employees_list')
    template_name = 'users/signup.html'
    permission_required = 'users.view_user'


class UserPanel(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_panel.html'


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm
    success_url = reverse_lazy('cal:list')


class EmployeesList(ListView):
    model = Employee
    template_name = 'users/employees.html'
    fields = ('name', 'surname', 'email', 'date_joined')


@superuser_required()
class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('users:employees_list')


@superuser_required()
class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'users/employee_update_form.html'
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy('users:employees_list')


@superuser_required()
class PasswordChangeUpdate(UpdateView):
    model = Employee
    template_name = 'users/employee_change_password_form.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users:employee_list')



