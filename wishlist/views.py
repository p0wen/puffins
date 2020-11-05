from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserWishlist, UserWishlistItem
from django.http import HttpResponseRedirect
from products.models import Product
from useraccount.models import UserAccount


@login_required
def view_wishlist(request):
    """ A view to return the shopping cart """
    user = UserAccount.objects.get(user=request.user)
    if request.user.is_authenticated:
        wishlist = list(UserWishlist.objects.filter(user_profile=user))
    print(wishlist)
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    item = get_object_or_404(Product, pk=product_id)
    user = UserAccount.objects.get(user=request.user)
    wishlist = UserWishlist.objects.get_or_create(user_profile=user)
    wished_products = UserWishlist.objects.get_or_create(wished_products=item)
    created = UserWishlistItem.objects.get_or_create(
                                        wished_products=item,
                                        user_profile=user,
                                        )
    for item in UserWishlistItem:
        if item in wished_products:
            wished_products.remove(item)
        else:
            wished_products.add(item)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
