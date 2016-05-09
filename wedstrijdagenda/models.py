from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.db import models
import datetime
from django.conf import settings

# Create your models here.
from django.template.defaultfilters import slugify

from vereniging.models import ZeilVereniging


class Wedstrijd(models.Model):
    start = models.DateTimeField(verbose_name="Start", blank=False)
    eind = models.DateTimeField(verbose_name="Eind", blank=False)
    vereniging = models.ForeignKey(ZeilVereniging)
    beschrijving = models.TextField(verbose_name="Beschrijving", blank=False)
    titel = models.CharField(max_length=150)
    slug = models.SlugField()
    deelnemers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.titel

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titel)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("zeilwedstrijd", kwargs={"slug": self.slug})
        # return "zeilwedstrijd/%s" % (self.slug)
