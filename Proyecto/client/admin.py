from django.contrib import admin
from client.models import Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'identity')
    search_fields = ('name', 'email', 'identity')
