from django.contrib.auth.models import Group as AuthGroup
from django.utils.translation import ugettext_lazy as _


class Group(AuthGroup):
    """
    Group model for users. Inherit Django Groups as proxy.
    """

    class Meta:
        proxy = True
        verbose_name = _('group')
        verbose_name_plural = _('groups')

        permissions = (
        )
