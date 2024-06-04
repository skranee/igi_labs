from django.contrib import admin
from app.models_app.employeeModel import UserEmployee, Employee


@admin.register(UserEmployee)
class UserEmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'isAdmin', 'createdAt', 'lastUpdate')
    list_filter = ('isAdmin',)
    search_fields = ('name', 'phone', 'email')
    fieldsets = (
        (None, {
            'fields': ('name', 'phone', 'email', 'password', 'isAdmin')
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'salary', 'photo', 'createdAt', 'lastUpdate')
    list_filter = ('position',)
    search_fields = ('position',)
    fieldsets = (
        (None, {
            'fields': ('position', 'salary', 'photo')
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
