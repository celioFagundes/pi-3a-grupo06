from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'nome', 'idade','sexo','data_nascimento')
    list_filter = ('email', 'sexo')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (['nome'])}),
        ('Permissions', {'fields': ([])}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'nome')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
