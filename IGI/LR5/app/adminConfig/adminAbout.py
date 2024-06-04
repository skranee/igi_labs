from django.contrib import admin
from app.models_app.aboutModel import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_filter = ('id',)
    search_fields = ('text',)
    fieldsets = (
        (None, {
            'fields': ('text', 'image')
        }),
    )
