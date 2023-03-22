from datetime import datetime, timedelta
import calendar
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView
from django.utils.safestring import mark_safe
from .forms import EventForm
from .models import Event
from .utils import QuickBookCalendar
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from salon.models import Salon
from users.models import Employee


class MainPage(TemplateView):
    template_name = 'cal/base.html'


class CalendarView(ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = QuickBookCalendar(d.year, d.month)

        cal_object = cal.cal_object(d.year, d.month)
        context['calendar'] = cal_object
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


class EventList(ListView):
    model = Event


class EventCreate(CreateView):
    model = Event


class EventDetail(DetailView):
    model = Event


class EventDelete(DeleteView):
    model = Event


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})


def get_employees(request):
    salon_id = request.GET.get('salon_id')
    salon = get_object_or_404(Salon, id=salon_id)
    employees = Employee.objects.filter(salon=salon)
    data = [{'id': e.id, 'name': e.name} for e in employees]
    return JsonResponse(data, safe=False)
