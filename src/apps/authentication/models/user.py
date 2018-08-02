import logging

from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

log = logging.getLogger(__name__)


class UserQuerySet(models.QuerySet):
    """
    Query set for User model.
    """

    def get_by_email(self, username):
        """Returns user by username or email for one search parameter."""
        email = username.lower()
        return self.get(username=email)


class UserManager(BaseUserManager):
    """
    Manager for User model.
    """

    def get_queryset(self):
        """Get User Query Set instead base queryset."""
        return UserQuerySet(self.model, using=self._db)

    def get_by_email(self, username):
        """Returns queryset for get user by username or email for one search parameter."""
        return self.get_queryset().get_by_email(username)


class User(AbstractUser):
    """
    Custom user model for all users.

    is_system - parameter for ident system users
    """
    email = models.EmailField(_('email address'), unique=True, db_index=True, default='')

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        permissions = (
        )

    def has_group(self, group_ids=None, group_names=None):
        """
        Check user in groups by group ids or group names.
        :param group_ids: List of group ids
        :param group_names: List of group names
        :return: boolean value of checking result
        """
        try:
            return self.groups.filter(Q(id__in=group_ids or []) | Q(name__in=group_names or [])). \
                exists()
        except Exception:
            log.warning('User {} has no groups!'.format(self.username))

            return False
