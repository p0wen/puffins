#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserAccount
from .forms import UserAccountForm
from checkout.models import Order
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Update failed.\
                    Please ensure the form is valid.')

    form = UserAccountForm(instance=profile)
    orders = profile.orders.all()

    template = 'useraccount/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)

@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
