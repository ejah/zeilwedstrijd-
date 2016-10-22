from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.db import models
import datetime
from django.conf import settings

# Create your models here.
from django.template.defaultfilters import slugify

from vereniging.models import ZeilVereniging

class WedstrijdType(models.Model):
    klasse = models.BooleanField(verbose_name="Eenheidsklasse", default=False)
    handicap = models.BooleanField(verbose_name="Open op handicap", default=False)
    jeugd = models.BooleanField(verbose_name="Jeugdwedstrijd", default=False)
    single_handed = models.BooleanField(verbose_name="Single handed", default=False)
    dual_handed = models.BooleanField(verbose_name="Dual handed", default=False)
    inshore = models.BooleanField(verbose_name="Inshore", default=False)
    nearshore = models.BooleanField(verbose_name="Near shore", default=False)
    offshore = models.BooleanField(verbose_name="Offshore", default=False)

    def __str__(self):
        name_list = [];
        fieldlist = self._meta.get_fields()
        for field in fieldlist:
            if field.get_internal_type() in ["BooleanField"]:
                if getattr(self, field.name):
                    name_list.append(field.verbose_name)
        return " ".join(name_list)

    class Meta:
        verbose_name_plural = "Wedstrijdtypen"

class Wedstrijd(models.Model):
    start = models.DateTimeField(verbose_name="Start", blank=False)
    eind = models.DateTimeField(verbose_name="Eind", blank=False)
    vereniging = models.ForeignKey(ZeilVereniging)
    beschrijving = models.TextField(verbose_name="Beschrijving", blank=False)
    titel = models.CharField(max_length=150)
    slug = models.SlugField()
    deelnemers = models.ManyToManyField(settings.AUTH_USER_MODEL)
    wedstrijd_type = models.ForeignKey(WedstrijdType)

    def __str__(self):
        return self.titel

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titel)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("zeilwedstrijd", kwargs={"slug": self.slug})
        # return "zeilwedstrijd/%s" % (self.slug)

    class Meta:
        verbose_name_plural = "Wedstrijden"
