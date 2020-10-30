from django.contrib import admin
from .models import Order, OrderLineItem, OrderStatus


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderStatus

class OrderStatusAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date_order_placed',
                       'delivery_cost', 'total_order',
                       'grand_total')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'total_order', 'grand_total',
              'stripe_pid')

    list_display = ('order_number', 'date_order_placed', 'first_name', 'last_name',
                    'total_order', 'delivery_cost',
                    'grand_total', 'total_tax', 'tax_rate')


admin.site.register(Order, OrderAdmin)