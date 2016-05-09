from django.contrib import admin
from .models import Gebruiker, ZeilVereniging, Adres
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin
class AdresAdmin(ModelAdmin):
    pass
admin.site.register(Adres, AdresAdmin)

class UserProfileInline(admin.StackedInline):
    model = Gebruiker


class UserAdmin(UserAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class ZVAdmin(ModelAdmin):
    pass
admin.site.register(ZeilVereniging, ZVAdmin)