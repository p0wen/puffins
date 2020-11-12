#!/usr/bin/python
# -*- coding: utf-8 -*-

from .models import BlogPost
from django.contrib import admin


class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    readonly_fields = ('slug',)


admin.site.register(BlogPost, BlogPostAdmin)
