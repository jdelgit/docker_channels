from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NotifierConfig(AppConfig):
    name = 'notifier'
    verbose_name = _('notifier')

    def ready(self):
        import notifier.signals
