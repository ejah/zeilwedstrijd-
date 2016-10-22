from django.contrib import admin

# Register your models here.
from wedstrijdagenda.models import Wedstrijd, WedstrijdType


class WedstrijdAdmin(admin.ModelAdmin):
    pass

admin.site.register(Wedstrijd, WedstrijdAdmin)

class WedstrijdTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(WedstrijdType, WedstrijdTypeAdmin)