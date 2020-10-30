from django.shortcuts import render, redirect


def checkout(request):
    """ A view to return the checkout page """

    return render(request, 'checkout/checkout.html')