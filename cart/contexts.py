from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import ProductVariant


def cart_content(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for productvariant, quantity in cart.items():
        lineitem = get_object_or_404(ProductVariant, pk=productvariant)
        print(lineitem.product.is_on_sale)
        if lineitem.product.is_on_sale or lineitem.product.avail_for_pre_order:
            price = lineitem.product.discount_price
        else:
            price = lineitem.product.price
        total += price * quantity
        product_count += quantity
        subtotal = price * quantity
        cart_items.append({
            'productvariant': productvariant,
            'quantity': quantity,
            'lineitem': lineitem,
            'subtotal': subtotal,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_FEE
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    total_tax = grand_total * Decimal(settings.TAX_RATE_PERCANTAGE / 100)

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'total_tax': total_tax,
        'tax_rate': settings.TAX_RATE_PERCANTAGE,
    }

    return context
