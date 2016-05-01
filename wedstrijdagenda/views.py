from django.shortcuts import render, render_to_response


# Create your views here.
from django.template import RequestContext
from schedule.periods import Month, Day
from schedule.views import calendar_by_periods
from schedule.models import Calendar, Event
from datetime import datetime


def homepage(request):
    cal, created = Calendar.objects.get_or_create(name="Zeil wedstrijden", slug = "zeil-wedstrijden")
    data = {"title":"Test wedstrijd", "start":datetime.now(), "end":datetime(2016, 5, 5)}
    event = Event(**data)
    event.save()
    cal.events.add(event)

    return calendar_by_periods(request=request, calendar_slug=cal.slug, periods=[Month, Day], template_name="schedule/calendar_month.html")