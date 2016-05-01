from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

# Create your views here.
# -- Verenigings views
from vereniging.models import ZeilVereniging, Gebruiker


class VCreateView(CreateView):
    model = ZeilVereniging

    def get_success_url(self):
        return reverse("vereniging", kwargs={"slug": self.object.slug})


class VDeleteView(DeleteView):
    model = ZeilVereniging
    success_url = reverse_lazy("verenigingen")


class VUpdateView(UpdateView):
    model = ZeilVereniging

    def get_success_url(self):
        return reverse("v-detail", kwargs={"slug": self.object.slug})


class VListView(ListView):
    model = ZeilVereniging


class VDetailView(DetailView):
    model = ZeilVereniging


# --- Gebruikers views

class GCreateView(CreateView):
    model = Gebruiker

    def get_success_url(self):
        return reverse("gebruikers", kwargs={"slug": self.object.slug})

class GDeleteView(DeleteView):
    model = Gebruiker
    success_url = reverse_lazy("home")

class GListView(ListView):
    model = Gebruiker

class GUpdateView(UpdateView):
    model = Gebruiker

    def get_success_url(self):
        return reverse("gebruikers", kwargs={"pk": self.object.pk})

class GDetailView(DetailView):
    model = Gebruiker
