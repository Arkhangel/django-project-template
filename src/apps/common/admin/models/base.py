from django.contrib import admin


class BaseAdminModel(admin.ModelAdmin):
    """
    Base Admin Model for protect delete operation.
    """

    def has_delete_permission(self, request, obj=None):  # pragma: no cover
        return False
