from django.contrib import admin
from app.models_app.productModel import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier', 'category', 'price', 'createdAt', 'lastUpdate')
    list_filter = ('category', 'supplier', 'createdAt')
    search_fields = ('name', 'category__name', 'supplier__name')
    fieldsets = (
        (None, {
            'fields': ('name', 'supplier', 'category', 'price', 'image')
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
