from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductVariant, ProductSize, ProductLine

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all().filter(discontinued=False)
    query = None
    category = None
    productline = None

    if request.GET:
        if 'category' and not 'productline' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name__icontains=category)
        elif 'productline' and not 'category' in request.GET:
            productline = request.GET['productline']
            products = products.filter(productline__name__icontains=productline)
        elif 'category' and 'productline' in request.GET:
            category = request.GET['category']
            productline = request.GET['productline']
            products = products.filter(category__name__contains=category).filter(productline__name__contains=productline)
            print(category, productline, products)


    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(productline__name__icontains=query) | Q(category__name__icontains=query) 
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'category': category,
        'productline': productline,
    }

    print(products)
    return render(request, 'products/products.html', context)

"""
def product_category(request, category_id):

    products = Product.objects.all().filter(discontinued=False).filter(Product.category==category_id)
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'products': products,
        'current_category': category,
    }

    return render(request, 'products/products.html', context)

"""

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
