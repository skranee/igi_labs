from django.contrib import admin
from app.models_app.newsModel import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'createdAt', 'lastUpdate')
    list_filter = ('title', 'createdAt')
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'image')
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
