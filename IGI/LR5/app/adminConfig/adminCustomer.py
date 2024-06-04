from django.contrib import admin
from app.models_app.customerModel import Customer, RegularCustomer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'phone')
    list_filter = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    fieldsets = (
        (None, {
            'fields': ('email', 'name', 'phone', 'password')
        }),
    )


@admin.register(RegularCustomer)
class RegularCustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'createdAt', 'lastUpdate')
    list_filter = ('createdAt',)
    search_fields = ('customer__name', 'customer__email', 'customer__phone')
    fieldsets = (
        (None, {
            'fields': ('customer',)
        }),
        ('Object info', {'fields': ('createdAt', 'lastUpdate')})
    )
