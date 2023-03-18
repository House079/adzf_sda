from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView
from .models import Salon
from .forms import SalonForm


# Create your views here.

def send_salon(request):
    form = SalonForm(request.POST or None)

    if form.is_valid():
        salon = form.save()
        return HttpResponseRedirect(request.path)
    salons = Salon.objects.all()
    return render(request, 'salon/salon.html', {'form': form, 'salons': salons})


class SalonList(ListView):
    model = Salon
    template_name = 'salon/salon.html'


class SalonUpdate(UpdateView):
    model = Salon
    template_name = 'salon/salon_update_form.html'
    fields = ('name', 'city', 'address', 'details')
    success_url = reverse_lazy('salon:send_salon')


class SalonDelete(DeleteView):
    model = Salon
    success_url = reverse_lazy('salon:send_salon')
