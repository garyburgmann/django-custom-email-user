from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from custom_email_user.models import User
from custom_email_user.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = (
        'id', 'email', 'username', 'first_name', 'last_name', 'is_staff',
    )
    readonly_fields = ('id',)
    fieldsets = (
        ((None), {
            'fields': (
                'id', 'email', 'username', 'password',
            )
        }),
        (('Personal info'), {
            'fields': (
                'first_name', 'last_name',
            )
        }),
        (('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups',
                'user_permissions',
            ),
        }),
        (('Important dates'), {
            'fields': (
                'last_login', 'date_joined',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2',)}
        ),
    )


# admin.site.register(User, CustomUserAdmin)
