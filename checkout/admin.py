#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderAdminInline,)

    readonly_fields = ('order_number',  'date_order_placed',
                       'delivery_cost', 'total_order',
                       'grand_total', 'total_tax', 'tax_rate',
                       'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'user_profile',
              'order_status', 'date_order_placed',
              'first_name', 'last_name', 'email', 'phone_number',
              'street_address1', 'street_address2',
              'zipcode', 'town_or_city', 'country',
              'delivery_cost', 'total_order', 'grand_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'order_status', 'date_order_placed',
                    'user_profile',
                    'total_order', 'delivery_cost',
                    'grand_total', 'total_tax', 'tax_rate')

    ordering = ('-date_order_placed',)


admin.site.register(Order, OrderAdmin)
