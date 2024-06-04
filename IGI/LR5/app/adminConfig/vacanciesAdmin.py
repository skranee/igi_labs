from django.contrib import admin
from app.models_app.vacancyModel import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'salary', 'createdAt', 'lastUpdate')
    list_filter = ('salary',)
    search_fields = ('position',)
    fieldsets = (
        (None, {
            'fields': ('position', 'description', 'salary')
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
