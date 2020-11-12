#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from products.models import Product
import random


def index(request):
    """ A view to return the index page """

    req_no_of_random_items = 4
    qs = Product.objects.filter(is_featured=True, discontinued=False)
    possible_ids = list(qs.values_list('id', flat=True))
    possible_ids = random.choices(possible_ids, k=req_no_of_random_items)
    random_featured_product = qs.filter(pk__in=possible_ids)
    context = {
        'featured': random_featured_product,
    }

    return render(request, 'home/index.html', context)
