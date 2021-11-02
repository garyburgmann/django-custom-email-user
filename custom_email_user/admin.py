# from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from .models import User
from .forms import (
    UserCreationForm,
    UserChangeForm
)


# @admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
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
            'fields': ('email', 'username', 'password1', 'password2',)
        }),
    )
