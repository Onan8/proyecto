from django.contrib import admin
from seller.models import Seller


# Register your models here.
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number_employee')
    search_fields = ('name', 'email', 'number_employee')
