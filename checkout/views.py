from django.shortcuts import render, redirect,\
                                reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_content

import stripe


def checkout(request):
    """ A view to return the checkout page """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request,
                       "There's nothing in your shopping cart at the moment")
        return redirect(reverse('cart'))
    current_cart = cart_content(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set in in your env?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
