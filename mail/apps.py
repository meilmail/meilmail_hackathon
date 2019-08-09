from django.apps import AppConfig
from django.conf import settings

class MailConfig(AppConfig):
    name = 'mail'

    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from . import operator
            operator.start()