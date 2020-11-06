from django.db import models
from products.models import Product
from useraccount.models import UserAccount


class UserWishlist(models.Model):
    user_profile = models.OneToOneField(UserAccount, on_delete=models.CASCADE,
                                     null=False, blank=False)
    wished_products = models.ManyToManyField(Product, related_name='userwishlists')
