import uuid
from django.db import models
from django.db.models import Sum
from decimal import Decimal
from django.conf import settings
from django_countries.fields import CountryField

from products.models import ProductVariant
from useraccount.models import UserAccount

STATUS_OPTIONS = [
    ('0', 'Order Received'),
    ('1', 'Order Accepted'),
    ('2', 'Preparing for delivery'),
    ('3', 'Dispatched'),
    ('4', 'Order Received'),
    ('C', 'Order Canceld'),
]


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    account_number = models.ForeignKey(UserAccount, on_delete=models.SET_NULL,
                                       null=True, blank=True, related_name='orders')
    order_status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default='0')
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    country = CountryField(blank_label='Country', null=False, blank=False)
    zipcode = models.CharField(max_length=20, null=True, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, blank=True)
    total_order = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total_tax = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    tax_rate = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date_order_placed = models.DateTimeField(auto_now_add=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.total_order = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.total_order < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = Decimal(settings.STANDARD_DELIVERY_FEE)
        else:
            self.delivery_cost = 0
        self.grand_total = self.total_order + self.delivery_cost
        self.tax_rate = settings.TAX_RATE_PERCENTAGE
        self.total_tax = Decimal(self.grand_total) * Decimal(self.tax_rate / 100)
        self.save()

    def save(self, *args, **kwargs):
        self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name="lineitems")
    productvariant = models.ForeignKey(ProductVariant, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0, editable=False)

    def save(self, *args, **kwargs):
        if self.productvariant.product.is_on_sale or self.productvariant.product.avail_for_pre_order:
            self.lineitem_total = self.productvariant.product.discount_price * self.quantity
        else:
            self.lineitem_total = self.productvariant.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ProductID {self.productvariant.product.name} on order {self.order.order_number}'
