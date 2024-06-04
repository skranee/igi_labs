from django.contrib import admin
from app.models_app.categoryModel import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'createdAt', 'lastUpdate')
    list_filter = ('name',)
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
