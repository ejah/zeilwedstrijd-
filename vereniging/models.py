from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from localflavor.generic.countries import iso_3166

# Create your models here.
from django.template.defaultfilters import slugify

class Adres(models.Model):
    woonplaats = models.CharField(max_length=50, blank=False)
    straatnaam = models.CharField(max_length=50, blank=True)
    huisnummer = models.CharField(max_length=10, blank=True)
    postbus = models.BooleanField(default=False)
    postbusnummer = models.CharField(max_length=10, blank=True)
    postcode = models.CharField(max_length=7, blank=False)
    land = models.CharField(max_length=20, blank=True)


class ZeilVereniging(models.Model):
    naam = models.CharField(max_length=50, unique=True)
    bezoekadres = models.ForeignKey(Adres, verbose_name="Bezoek adres", related_name="bezoekadres", null=True, blank=True)
    postadres = models.ForeignKey(Adres, verbose_name='Post adres', related_name="postadres", null=True, blank=True)
    slug = models.SlugField(default="", blank=True)
    # ToDo: Details van de vereniging toevoegen aan het model

    def __str__(self):
        return "{}: {}:".format(self.naam, self.bezoekadres or "")

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

    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    usertype = models.IntegerField(default=0, choices=USER_TYPES)
    adres = models.ForeignKey(Adres, null=True)
    vereniging = models.ForeignKey(ZeilVereniging, null=True)

    def __str__(self):
        typename = [x[1] for x in self.USER_TYPES if x[0] == self.usertype].pop()
        return "{}: {}: {}".format(self.user.last_name, self.vereniging.naam, typename)

