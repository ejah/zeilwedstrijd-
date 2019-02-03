# File forms created on: 10-05-16 by: ejah
import datetime

from django.forms import ModelForm, CharField
from bootstrap3_datetime.widgets import DateTimePicker
from bootstrap_datepicker_plus import DateTimePickerInput

from wedstrijdagenda.models import Wedstrijd


class CreateWedstrijdForm(ModelForm):
    class Meta:
        model = Wedstrijd
        fields = ["titel", "start", "eind", "beschrijving", "vereniging"]
        widgets = {
            "start": DateTimePickerInput(
                format=" D-MM-YYYY HH:mm",
                options={"sideBySide": True, "useCurrent": True, "calendarWeeks":True, }),
            "eind": DateTimePickerInput(
                format="D-MM-YYYY HH:mm",
                options={"sideBySide": True, "useCurrent": True, "calendarWeeks":True, })
        }
