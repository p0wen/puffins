#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def display_blogcontent(request):
    """
    Get all Blog posts for overview
    Based on this tutorial:
    https://medium.com/swlh/building-your-own-django-blog-part-2-78adbc516992
    """

    blogposts = BlogPost.objects.all()
    template = 'blog/blog.html'
    context = {
        'blogposts': blogposts,
        }

    return render(request, template, context)


def show_post(request, slug):
    """
    Display specific blog post based on
    provided slug in request.
    Based on this tutorial:
    https://medium.com/swlh/building-your-own-django-blog-part-2-78adbc516992
    """

    blogpost = get_object_or_404(BlogPost, slug=slug)
    template = 'blog/show_post.html'
    context = {
        'blogpost': blogpost
        }
    return render(request, template, context)
