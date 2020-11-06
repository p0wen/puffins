from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from products.models import Product
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
    wish = get_object_or_404(Product, pk=product_id)
    user = UserAccount.objects.get(user=request.user)
    wishlist = Product.objects.filter(userwishlists__user_profile=user)

    if wish in wishlist:
        wish.userwishlists.remove(user.id)
    else:
        wish.userwishlists.add(user.id)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
