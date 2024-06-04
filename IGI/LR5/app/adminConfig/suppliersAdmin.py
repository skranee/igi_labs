from django.contrib import admin
from app.models_app.supplierModel import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'name', 'deliveryTime', 'foundationDate', 'createdAt', 'lastUpdate')
    list_filter = ('country', 'deliveryTime')
    search_fields = ('country', 'name')
    fieldsets = (
        (None, {
            'fields': ('country', 'name', 'deliveryTime', 'foundationDate')
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
