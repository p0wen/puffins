#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, reverse, HttpResponse
from django.template.loader import render_to_string
from collections import OrderedDict
from datetime import datetime

import json


def view_cart(request):
    """ A view to return the shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request):
    """
    Add a productvariant to cart and
    provide updated cart context through the ajax call
    for the side drawer cart
    Ajax & Django Tutorial:
    https://realpython.com/django-and-ajax-form-submissions/
    """

    if request.method == 'POST':
        productvariant = request.POST.get('productvariant')
        cart = request.session.get('cart', {})
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if productvariant in list(cart.keys()):
            cart[productvariant]['qty'] += 1
            cart[productvariant]['date_created'] = now
        else:
            cart[productvariant] = {'qty': 1, 'date_created': now}
        orderd_cart = OrderedDict(
            sorted(cart.items(),
                   key=lambda x: x[1]['date_created'], reverse=True))
        request.session['cart'] = orderd_cart
        render_cart = render_to_string('./includes/sideDrawerContent.html',
                                       request=request)
        return HttpResponse(
            render_cart,
            content_type="text/html"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def increase_quantity_by_one(request, productvariant):
    """
    Increase Quanity by 1
    """

    cart = request.session.get('cart', {})
    if productvariant in list(cart.keys()):
        cart[productvariant]['qty'] += 1

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def decrease_quantity_by_one(request, productvariant):
    """
    Decrease Quanity by 1
    """

    cart = request.session.get('cart', {})
    if productvariant in list(cart.keys()):
        if cart[productvariant]['qty'] > 1:
            cart[productvariant]['qty'] -= 1
        else:
            cart.pop(productvariant)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, productvariant):
    """
    Remove the item from the shopping cart
    """

    cart = request.session.get('cart', {})

    if productvariant in list(cart.keys()):
        cart.pop(productvariant)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
