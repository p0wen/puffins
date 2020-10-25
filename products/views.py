from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductVariant, ProductSize

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    active_products = products.filter(discontinued=False)
    context = {
        'products': active_products,
    }

    print(products)
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    product_variants = ProductVariant.objects.all().filter(product_id=product_id)
    
    print(product_variants)
    context = {
        'product': product,
        'product_variants': product_variants,
    }

    return render(request, 'products/product_detail.html', context)
