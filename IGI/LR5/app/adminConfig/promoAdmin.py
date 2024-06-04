from django.contrib import admin
from app.models_app.promoModel import Promo


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'valid_until', 'archived', 'code', 'discount', 'createdAt', 'lastUpdate')
    list_filter = ('valid_until', 'archived')
    search_fields = ('value', 'code')
    fieldsets = (
        (None, {
            'fields': ('value', 'valid_until', 'archived', 'code', 'discount')
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
