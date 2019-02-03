import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.urls import reverse

# Create your views here.
from django.template import RequestContext, loader
from django.views.generic import DetailView, CreateView
from schedule.models import Calendar, Event
from datetime import datetime

from wedstrijdagenda.forms import CreateWedstrijdForm
from wedstrijdagenda.models import Wedstrijd, WedstrijdType

actief_filter = {}

@ensure_csrf_cookie
def homepage(request):
    # cal, created = Calendar.objects.get_or_create(name="Zeil wedstrijden", slug="zeil-wedstrijden")
    # if created:
    #     data = {"title": "Test wedstrijd", "start": datetime.now(), "end": datetime(2016, 5, 5)}
    #     event = Event(**data)
    #     event.save()
    #     cal.events.add(event)
    # Voeg de filtervelden toe aan de context
    wedstrijd_type_list = {}
    for field in WedstrijdType._meta.get_fields():
        if field.get_internal_type() in ["BooleanField"]:
            wedstrijd_type_list[field.name] = field.verbose_name
    template = loader.get_template('calendar_base.html')
    context = {
        'filter':wedstrijd_type_list,
    }
    return HttpResponse(template.render(context, request))


def api_wedstrijden(request):
    wedstrijden = Wedstrijd.objects.all()
    ws_lijst = []
    filterlijst = []
    for fname, fstatus in actief_filter.items():
        if not fstatus:
            filterlijst.append(fname)
    for wedstrijd in wedstrijden:
        if not wedstrijd.is_filtered(filterlijst):
            ws_lijst.append(
                {"id": wedstrijd.pk,
                 "start": wedstrijd.start.isoformat(),
                 "end": wedstrijd.eind.isoformat(),
                 "title": wedstrijd.titel,
                 "beschrijving": wedstrijd.beschrijving,
                 "url": "zeilwedstrijd/%s/" % wedstrijd.slug,
                 })
    return HttpResponse(json.dumps(ws_lijst), content_type="application/json")

def api_filter_wedstrijden(request):
    # Browser stuurt een JSON dict met alle filters als key - value pairs

    if request.method == 'POST':
        filter_id = request.POST.get("filter_id");
        filter_val = request.POST.get("filter_val") in ['true', 'True', 'T', '1'];
        if request.user.is_authenticated():
            # todo: if the user is authenticated, store the filter data in it's profile
            # en update het actieve filter
            actief_filter[filter_id] = filter_val
        else:
            actief_filter[filter_id] = filter_val

    return HttpResponse('ok')


# todo: afmaken van de Ajax communicatie.

@login_required
def inschrijven(request, slug):
    wedstrijd = get_object_or_404(Wedstrijd, slug=slug)
    cu = request.user
    if not cu in wedstrijd.deelnemers.filter(pk=cu.pk):
        wedstrijd.deelnemers.add(cu)
    return redirect(wedstrijd)


@login_required
def uitschrijven(request, slug):
    wedstrijd = get_object_or_404(Wedstrijd, slug=slug)
    cu = request.user
    if cu in wedstrijd.deelnemers.filter(pk=cu.pk):
        wedstrijd.deelnemers.remove(cu)
    return redirect(wedstrijd)


class WedstrijdDetailView(DetailView):
    model = Wedstrijd
    slug_field = "slug"


class WedstrijdCreateView(CreateView):
    model = Wedstrijd
    # fields = ["start", "eind", "titel", "beschrijving", "vereniging"]
    success_url = "/"
    form_class = CreateWedstrijdForm

