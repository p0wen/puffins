#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Product, Category, ProductLine, ProductSize, ProductVariant


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'display_text',
        'image',
        'image_url',
        )


class ProductLineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'display_text',
        )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'productline',
        'name',
        'display_text',
        'price',
        'discount_price',
        'is_on_sale',
        'avail_for_pre_order',
        'discontinued',
        'image',
        'image_url',
        'description',
        'date_of_dispatch',
        'color',
        'material_1',
        'material_2',
        'is_featured',
        )


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = (
        'shirt_size',
        )


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'size',
        'quantity',
        )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)
admin.site.register(ProductLine, ProductLineAdmin)
