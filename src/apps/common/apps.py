from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CommonConfig(AppConfig):
    name = 'src.apps.common'
    label = 'common'

    def ready(self):
        self.verbose_name = _('Common')
