from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        'order_number',
        'date',
        'order_total',
        'stripe_pid'
    )
    list_display = (
        'order_number',
        'stripe_pid',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'date',
        'order_total'
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
