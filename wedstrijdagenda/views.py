import json

from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
from schedule.models import Calendar, Event
from datetime import datetime

from wedstrijdagenda.models import Wedstrijd


def homepage(request):
    cal, created = Calendar.objects.get_or_create(name="Zeil wedstrijden", slug="zeil-wedstrijden")
    if created:
        data = {"title": "Test wedstrijd", "start": datetime.now(), "end": datetime(2016, 5, 5)}
        event = Event(**data)
        event.save()
        cal.events.add(event)

    return render_to_response("home.html")


def api_wedstrijden(request):
    wedstrijden = Wedstrijd.objects.all()
    ws_lijst = []
    for wedstrijd in wedstrijden:
        ws_lijst.append(
            {"id": wedstrijd.pk,
             "start": wedstrijd.start.isoformat(),
             "end": wedstrijd.eind.isoformat(),
             "title": wedstrijd.titel,
             "beschrijving": wedstrijd.beschrijving,
             "url": wedstrijd.get_absolute_url(),
             })
    return HttpResponse(json.dumps(ws_lijst), content_type="application/json")
