from django.urls import reverse
from django.db import models
from django.conf import settings
from localflavor.generic.countries import iso_3166

# Create your models here.
from django.template.defaultfilters import slugify

class Adres(models.Model):
    woonplaats = models.CharField(max_length=50, blank=False)
    straatnaam = models.CharField(max_length=50, blank=True)
    huisnummer = models.CharField(max_length=10, blank=True)
    postcode = models.CharField(max_length=7, blank=False)
    land = models.CharField(max_length=20, blank=True)
    is_standaard = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.woonplaats, self.postcode)

    class Meta:
        abstract=True
        verbose_name_plural="Adressen"
        verbose_name="Adres"

class VerenigingsAdres(Adres):
    vereniging = models.ForeignKey("ZeilVereniging", models.CASCADE, blank=True, null=True)

class GebruikersAdres(Adres):
    gebruiker = models.ForeignKey("Gebruiker", models.CASCADE, blank=True, null=True)


class ZeilVereniging(models.Model):
    naam = models.CharField(max_length=50, unique=True)
    # bezoekadres = models.ForeignKey(Adres, verbose_name="Bezoek adres", related_name="bezoekadres", null=True, blank=True)
    # postadres = models.ForeignKey(Adres, verbose_name='Post adres', related_name="postadres", null=True, blank=True)
    slug = models.SlugField(default="", blank=True)
    # ToDo: Details van de vereniging toevoegen aan het model

    def __str__(self):
        return "{}".format(self.naam)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.naam)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("vereniging", kwargs={"slug": self.slug})

    class Meta:
        order_with_respect_to = 'naam'
        verbose_name_plural = "Zeil verenigingen"
        verbose_name = "Zeil vereniging"


class Gebruiker(models.Model):
    """
    Dit is een profiel van een gebruiker.
    Er zijn twee soorten:
    - normale gebruikers;
    - verenigingen;
    De laatste krijgen andere mogelijkheden in de app.
    """
    # Todo: Details als telefoon, email etc voegen we later toe

    USER_TYPES = [
        (0, "Normaal"),
        (1, "Vereniging"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.SET_NULL, primary_key=True, blank=True, null=True)
    usertype = models.IntegerField(default=0, choices=USER_TYPES)
    vereniging = models.ForeignKey(ZeilVereniging, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return " ".format(self.user.last_name, self.user.first_name)

