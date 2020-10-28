from django.shortcuts import render, redirect

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
