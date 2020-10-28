from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_cart(request):
    """ A view to return the shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request):
    """ Add a productvariant to cart """

    productvariant = request.POST.get('productvariant')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if productvariant in list(cart.keys()):
        cart[productvariant] += 1
    else:
        cart[productvariant] = 1

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def update_cart(request, productvariant):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[productvariant] = quantity
    else:
        cart.pop(productvariant)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, productvariant):
    """Remove the item from the shopping cart"""

    cart = request.session.get('cart', {})
    cart.pop(productvariant)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
