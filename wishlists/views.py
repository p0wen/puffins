#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from products.models import Product
from .models import UserWishlist
from useraccount.models import UserAccount


@login_required
def view_wishlist(request):
    """ A view to return the shopping cart """
    user = UserAccount.objects.get(user=request.user)
    wishlist = Product.objects.filter(userwishlists__user_profile=user)
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'wishlists/wishlist.html', context)


@login_required
def add_wish(request, product_id):
    """
    Allows users to add or remove a product to/from their personal wishlist.\n
    """

    wish = get_object_or_404(Product, pk=product_id)
    user = UserAccount.objects.get(user=request.user)
    wishlist_user, created = UserWishlist.objects.get_or_create(
        user_profile=user)
    wishlist = Product.objects.filter(userwishlists__user_profile=user)

    if created:
        wish.userwishlists.add(wishlist_user.id)
    else:
        if wish in wishlist:
            wish.userwishlists.remove(wishlist_user.id)
        else:
            wish.userwishlists.add(wishlist_user.id)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
