from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserWishlist
from django.http import HttpResponseRedirect
from products.models import Product
from useraccount.models import UserAccount


@login_required
def view_wishlist(request):
    """ A view to return the shopping cart """
    profile = get_object_or_404(UserAccount, user=request.user)
    wishlist = UserWishlist.objects.all().filter(user_profile=profile)
    print(wishlist)
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'wishlists/wishlist.html', context)


def add_to_wishlist(request, product_id):
    wish = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserAccount, user=request.user)
    wished_product, created = UserWishlist.objects.get_or_create(
                                                        wished_products=wish,
                                                        user_profile=profile)

    for item in wished_product:
        print(item)
        if wish in wished_product:
            print("i found ", wish, " and removed it")
            wished_product.remove(wish)
        else:
            wished_product.add(wish)
            print("i found your wish", wish)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
