from datetime import datetime, timedelta
import calendar
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
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
from django.contrib.auth.decorators import user_passes_test


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()


class CalendarView(LoginRequiredMixin, ListView):
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


class EventList(LoginRequiredMixin, ListView):
    model = Event

    def get_queryset(self):
        queryset = super().get_queryset()
        self.query = self.request.GET.get('q')
        if self.query:
            queryset = queryset.filter(
                Q(title__icontains=self.query) | Q(description__icontains=self.query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query  # Add the query variable to the context
        return context

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event


class EventDetail(LoginRequiredMixin, DetailView):
    model = Event


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/'


@login_required()
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


@login_required()
def get_employees(request):
    salon_id = request.GET.get('salon_id')
    salon = get_object_or_404(Salon, id=salon_id)
    employees = Employee.objects.filter(salon=salon)
    data = [{'id': e.id, 'name': e.username} for e in employees]
    return JsonResponse(data, safe=False)


@login_required()
def get_salons(request):
    salons = Salon.objects.all()
    data = [{'id': s.id, 'name': s.name} for s in salons]
    return JsonResponse(data, safe=False)


@login_required()
def get_events_at_day(request):
    selected_date = request.GET.get('day')
    selected_employee = request.GET.get('employee')
    selected_salon = request.GET.get('salon')

    selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()

    if selected_salon == 'none':
        events = Event.objects.filter(day=selected_date, employee=None, salon=selected_salon).order_by('start_time')
    else:
        events = Event.objects.filter(day=selected_date, employee=selected_employee, salon=selected_salon).order_by('start_time')

    data = [
        {
            'title': ev.title,
            'start_time': ev.start_time,
            'end_time': ev.end_time,
            'salon': ev.salon.name,
            'employee': ev.employee.name
        } for ev in events]
    return JsonResponse(data, safe=False)