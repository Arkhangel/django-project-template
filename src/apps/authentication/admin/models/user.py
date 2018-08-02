from django.contrib.auth import admin as auth_admin
from django.utils.translation import ugettext_lazy as _

from src.apps.common.admin.models import BaseAdminModel


class UserAdminModel(BaseAdminModel, auth_admin.UserAdmin):
    """
    Admin model for User. Inherits BaseAdminModel and UserAdmin (Django).
    """

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Personal info'), {'fields': ('first_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
