from django.contrib import admin
from .models import Gebruiker, ZeilVereniging, VerenigingsAdres, GebruikersAdres, Adres
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin


class AdresAdmin(ModelAdmin):
    pass

class AdresInline(admin.StackedInline):
    model = VerenigingsAdres
    max_num = 1
    extra = 1

admin.site.register(VerenigingsAdres, AdresAdmin)


class UserProfileInline(admin.StackedInline):
    model = Gebruiker

# class UserAdmin(UserAdmin):
#     inlines = [UserProfileInline]

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)


class ZVAdmin(ModelAdmin):
    inlines = [AdresInline,]
    fields = ["naam",]

admin.site.register(ZeilVereniging, ZVAdmin)