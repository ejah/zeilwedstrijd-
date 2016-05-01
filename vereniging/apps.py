from django.apps import AppConfig


class VerenigingConfig(AppConfig):
    name = 'vereniging'

    def ready(self):
        from . import signals
