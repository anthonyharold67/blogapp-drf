from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('image', 'bio')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('image', 'bio')}),
    )


admin.site.unregister(User)
admin.site.register(User, UserUserAdmin)