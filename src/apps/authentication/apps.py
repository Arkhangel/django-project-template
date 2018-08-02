from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AuthenticationConfig(AppConfig):
    name = 'src.apps.authentication'
    label = 'authentication'

    def ready(self):
        self.verbose_name = _('Authentication')
