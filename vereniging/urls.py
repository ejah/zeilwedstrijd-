# File urls created on: 30-04-16 by: ejah
from django.conf.urls import url
from . import views


v_urls = [
    url(r"^$", views.VListView.as_view(), name="verenigingen"),
    url(r"^(?P<slug>\w+/$)", views.VDetailView.as_view(), name="v-detail"),
    url(r"^(?P<slug>\w+/delete)", views.VDeleteView.as_view(), name="v-delete"),
    url(r"^(?P<slug>\w+/update)", views.VUpdateView.as_view(), name="v-update"),
]