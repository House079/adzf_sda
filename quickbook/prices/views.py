from django.urls import reverse_lazy
from .models import EventType
from django.views.generic import ListView, CreateView
from .forms import EventTypeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


def send_event(request):
    form = EventTypeForm(request.POST or None)

    if form.is_valid():
        event_type = form.save()
        return HttpResponseRedirect(request.path)
    event_types = EventType.objects.all()
    return render(request, 'prices/prices.html', {'form': form, 'event_types': event_types})


class EventTypesList(EventType, ListView):
    model = EventType
    template_name = 'prices/prices.html'


class CreateEvent(CreateView):
    form_class = EventTypeForm
    success_url = reverse_lazy('prices:prices')
    template_name = 'prices/eventtype_form.html'

