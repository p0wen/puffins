from django.contrib import admin
from .models import Order, OrderLineItem, OrderStatus


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderStatus


class OrderStatusAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline, OrderStatusAdminInline)

    readonly_fields = ('order_number', 'date_order_placed',
                       'delivery_cost', 'total_order',
                       'grand_total', 'total_tax', 'tax_rate')

    fields = ('order_number', 'date_order_placed', 'first_name',
              'last_name', 'email', 'phone_number',
              'street_address1', 'street_address2',
              'zipcode', 'town_or_city', 'country',
              'delivery_cost', 'total_order', 'grand_total')

    list_display = ('order_number', 'date_order_placed', 'first_name',
                    'last_name',
                    'total_order', 'delivery_cost',
                    'grand_total', 'total_tax', 'tax_rate')


admin.site.register(Order, OrderAdmin)
