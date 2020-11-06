from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name="wishlist"),
    path('add_wish/<product_id>', views.add_wish, name="add_wish"),
]
