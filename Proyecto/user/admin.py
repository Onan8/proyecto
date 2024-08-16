from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

#modifica  el user por defecto de django
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'name', 'number_employee', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'age', 'number_employee', 'phone', 'address', 'number_id')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'age', 'number_employee', 'phone', 'address', 'number_id', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'name', 'number_employee')
    ordering = ('email',)
    filter_horizontal = ()  # Elimina los filtros horizontales que no se aplican

admin.site.register(User, UserAdmin)
