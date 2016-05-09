"""zeilwedstrijd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from vereniging.urls import v_urls
from wedstrijdagenda import views
from wedstrijdagenda.views import api_wedstrijden, WedstrijdDetailView, inschrijven, uitschrijven

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^verenigingen/', include(v_urls)),
    url(r'^$', views.homepage, name="home"),
    # url(r'^schedule/', include('schedule.urls')),
    url(r'^api/wedstrijden', api_wedstrijden, name="wedstrijden"),
    url(r'^zeilwedstrijd/(?P<slug>[a-zA-Z0-9\-]+)/$', WedstrijdDetailView.as_view(), name="zeilwedstrijd"),
    url(r'^zeilwedstrijd/(?P<slug>[a-zA-Z0-9\-]+)/inschrijven', inschrijven, name="inschrijven"),
    url(r'^zeilwedstrijd/(?P<slug>[a-zA-Z0-9\-]+)/uitschrijven', uitschrijven, name="uitschrijven"),

]
