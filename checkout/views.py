from django.shortcuts import render, redirect,\
                                reverse, get_object_or_404,\
                                HttpResponse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from products.models import ProductVariant
from .models import Order, OrderLineItem
from cart.contexts import cart_content

import stripe
import json


def checkout(request):
    """ A view to return the checkout page """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        print('Trying to save the order')
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'zipcode': request.POST['zipcode'],
            'town_or_city': request.POST['town_or_city'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    productvariant = get_object_or_404(ProductVariant,
                                                       pk=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        productvariant=productvariant,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except ProductVariant.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your \
                        bag wasn't found in our database."
                        "Please call us for assitance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            print('Something went wrong')
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request,
                           "There's nothing in your \
                           shopping cart at the moment")
            return redirect(reverse('cart'))
        current_cart = cart_content(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

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


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)