from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ZW_User

class ZW_UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=ZW_User
        fields=("title", "first_name", "last_name", "email", "username", "stays_anonymous")


class ZW_UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = ZW_User
        fields = ("title", "first_name", "last_name", "email", "username", "stays_anonymous")

