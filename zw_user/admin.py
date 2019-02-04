from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ZW_UserCreationForm, ZW_UserChangeForm
from .models import ZW_User

class ZW_UserAdmin(UserAdmin):
    add_form = ZW_UserCreationForm
    form = ZW_UserChangeForm
    model = ZW_User
    list_display = ['title', 'first_name', 'last_name','email', 'username', 'stays_anonymous']

admin.site.register(ZW_User, ZW_UserAdmin)
