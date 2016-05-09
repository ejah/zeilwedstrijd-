from django.core.urlresolvers import reverse
from django.db import models
import datetime

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

    def __str__(self):
        return self.titel

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titel)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("zeilwedstrijd", kwargs={"slug": self.slug})