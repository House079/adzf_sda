from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from .models import Salon
from .forms import SalonForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin


def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser
        return WrappedClass
    return wrapper


def staff_user_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_staff
        return WrappedClass
    return wrapper


@login_required()
def send_salon(request):
    form = SalonForm(request.POST or None)

    if form.is_valid():
        salon = form.save()
        return HttpResponseRedirect('/salon')
    salons = Salon.objects.all()
    return render(request, 'salon/salon.html', {'form': form, 'salons': salons})


@staff_user_required()
class SalonList(ListView, PermissionRequiredMixin):
    model = Salon
    template_name = 'salon/salon_list.html'
    permission_required = 'salon.view_salon'


@staff_user_required()
class SalonDetail(DetailView, PermissionRequiredMixin):
    model = Salon
    permission_required = 'salon.view_salon'


@superuser_required()
class SalonUpdate(UpdateView):
    model = Salon
    template_name = 'salon/salon_update_form.html'
    fields = ('name', 'city', 'address', 'details')
    labels = {
        'name': 'Nazwa',
        'city': 'Miasto',
        'address': 'Adres',
        'details': 'Szczegóły'
    }
    success_url = reverse_lazy('salon:send_salon')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].label = self.labels['name']
        form.fields['city'].label = self.labels['city']
        form.fields['address'].label = self.labels['address']
        form.fields['details'].label = self.labels['details']
        return form

@superuser_required()
class SalonDelete(DeleteView):
    model = Salon
    success_url = reverse_lazy('salon:list')
