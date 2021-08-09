from django.apps import AppConfig


class MegaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mega'

    def ready(self):
        from . import signals