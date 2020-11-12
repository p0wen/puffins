#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=254)
    display_text = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class ProductLine(models.Model):
    name = models.CharField(max_length=50)
    display_text = models.CharField(max_length=254)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    productline = models.ForeignKey('ProductLine', on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    display_text = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[
                                MinValueValidator(0.01)])
    discount_price = models.DecimalField(max_digits=6, decimal_places=2,
                                         validators=[MinValueValidator(0.01)],
                                         blank=True)
    is_on_sale = models.BooleanField(default=False)
    avail_for_pre_order = models.BooleanField(default=False)
    date_of_dispatch = models.CharField(max_length=254, blank=True, null=True)
    discontinued = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_featured = models.BooleanField(default=False, null=True, blank=True)
    color = models.CharField(max_length=254, null=True)
    material_1 = models.CharField(max_length=254, null=True, blank=True)
    material_2 = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        ordering = ["-avail_for_pre_order"]

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    SIZE_CHOICES = [
        ('NO', 'None'),
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    shirt_size = models.CharField(max_length=2, choices=SIZE_CHOICES)

    def __str__(self):
        return self.shirt_size


class ProductVariant(models.Model):
    """ Model for product size and quantity """

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size = models.ForeignKey('ProductSize', on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0.0)])

    class Meta:
        unique_together = ["product", "size"]

    def __str__(self):
        return self.pk
