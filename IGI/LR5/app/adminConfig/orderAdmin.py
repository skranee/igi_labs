from django.contrib import admin
from app.models_app.orderModel import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'createdAt', 'lastUpdate')
    list_filter = ('product', 'customer', 'createdAt')
    search_fields = ('product__name', 'customer__name')
    fieldsets = (
        (None, {
            'fields': ('product', 'customer')
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
