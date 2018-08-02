from django.contrib import admin

from src.apps.common.admin.models import BaseAdminModel


class GroupAdminModel(BaseAdminModel, admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
