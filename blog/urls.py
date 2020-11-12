#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.urls import path
from . import views


urlpatterns = [
    path('', views.display_blogcontent, name="blog"),
    path('<str:slug>', views.show_post, name="show_post"),
]
