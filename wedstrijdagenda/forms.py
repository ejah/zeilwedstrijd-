# File forms created on: 10-05-16 by: ejah
import datetime

from django.forms import ModelForm, CharField
from bootstrap3_datetime.widgets import DateTimePicker

from wedstrijdagenda.models import Wedstrijd


class CreateWedstrijdForm(ModelForm):
    class Meta:
        model = Wedstrijd
        fields = ["titel", "start", "eind", "beschrijving", "vereniging"]
        widgets = {
            "start": DateTimePicker(
                format=" D-MM-YYYY HH:mm",
                options={"sideBySide": True, "useCurrent": True, "calendarWeeks":True, }),
            "eind": DateTimePicker(
                format="D-MM-YYYY HH:mm",
                options={"sideBySide": True, "useCurrent": True, "calendarWeeks":True, })
        }
