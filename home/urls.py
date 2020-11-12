#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home")
]
