from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name="view_cart"),
    path('add/', views.add_to_cart, name="add_to_cart"),
    path('increase_qty/<productvariant>/', views.increase_quantity_by_one, name='increase_quantity_by_one'),
    path('decrease_qty/<productvariant>/', views.decrease_quantity_by_one, name='decrease_quantity_by_one'),
    path('remove/<productvariant>/',
         views.remove_from_cart,
         name='remove_from_cart'),
]
