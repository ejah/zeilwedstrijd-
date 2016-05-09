from django.contrib import admin

# Register your models here.
from wedstrijdagenda.models import Wedstrijd


class WedstrijdAdmin(admin.ModelAdmin):
    pass

admin.site.register(Wedstrijd, WedstrijdAdmin)