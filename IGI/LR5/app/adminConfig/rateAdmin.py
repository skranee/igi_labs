from django.contrib import admin
from app.models_app.rateModel import Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'rate', 'createdAt', 'lastUpdate')
    list_filter = ('rate',)
    search_fields = ('author__name', 'text')
    fieldsets = (
        (None, {
            'fields': ('author', 'text', 'rate')
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
