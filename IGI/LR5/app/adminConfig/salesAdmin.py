from django.contrib import admin
from app.models_app.salesModel import Sales


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'salePrice', 'customer', 'address', 'createdAt', 'lastUpdate')
    list_filter = ('customer', 'createdAt')
    search_fields = ('customer__name', 'address')
    filter_horizontal = ('products',)
    fieldsets = (
        (None, {
            'fields': ('products', 'salePrice', 'customer', 'address')
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
