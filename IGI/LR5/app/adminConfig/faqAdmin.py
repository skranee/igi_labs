from django.contrib import admin
from app.models_app.faqModel import Faq


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'createdAt', 'lastUpdate')
    list_filter = ('title',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'text')
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
