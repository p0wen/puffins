#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import slugify
from useraccount.models import UserAccount


class BlogPost(models.Model):
    """
    Blogpost can be stored through the admin and are rendered
    Based on this tutorial:
    https://medium.com/swlh/building-your-own-django-blog-part-2-78adbc516992
    """

    author = models.ForeignKey(UserAccount,
                               on_delete=models.CASCADE,
                               null=False, blank=True)
    title = models.CharField(max_length=120,
                             null=True, blank=False)
    subtitle = models.CharField(max_length=180,
                                null=True, blank=False)
    body = models.TextField()
    slug = models.SlugField(unique=True,
                            max_length=250, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    title_image = models.ImageField(null=True, blank=True)
    title_image_url_1 = models.URLField(max_length=1024,
                                        null=True, blank=True)
    content_image_1 = models.ImageField(null=True, blank=True)
    content_image_url_1 = models.URLField(max_length=1024,
                                          null=True, blank=True)
    content_image_2 = models.ImageField(null=True, blank=True)
    content_image_url_2 = models.URLField(max_length=1024,
                                          null=True, blank=True)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        """
        Generates a unique slug based on the title
        Tutorial:
        https://simpleit.rocks/python/django/generating-slugs-automatically-in-django-easy-solid-approaches/
        """

        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while BlogPost.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the slug
        if it hasn't doesn't exist yet.
        """

        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
