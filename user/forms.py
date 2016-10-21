# File forms created on: 11-05-16 by: ejah
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from .utils import ActivationMailFormMixin
import logging
from django import forms

logger = logging.getLogger(__name__)


class UserCreationForm(ActivationMailFormMixin, BaseUserCreationForm):
    mail_validation_error = ("De gebruiker is aangemaakt. "
                             "Het is niet gelukt om de activerings email te versturen.\n"
                             "Probeer het later nog eens of stuur een bericht aan de beheerder van deze site.")

    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "email"]

    def save(self, **kwargs):
        user = super().save(commit=False)
        if not user.pk:
            user.is_active = False
            send_mail = True
        else:
            send_mail = False
        user.save()
        self.save_m2m()
        if send_mail:
            self.send_mail(user=user, **kwargs)
        return user

class ResendActivationEmailForm(ActivationMailFormMixin, forms.Form):

    email = forms.EmailField()
    mail_validation_error = "Helaas kan de activeringsemail niet opnieuw worden verstuurd. "\
        "Probeer het op een later moment nog eens. Onze excuses."

    def save(self, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(email=self.cleaned_data(['email']))
        except:
            logger.warning('Resend activation: geen gebruiker met email {}.'.format(self.cleaned_data(['email'])))
            return None
        self.send_mail(user=user, **kwargs)
        return user