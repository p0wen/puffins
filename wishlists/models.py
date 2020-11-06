from django.db import models
from products.models import Product
from useraccount.models import UserAccount


class UserWishlist(models.Model):
    user_profile = models.ForeignKey(UserAccount, on_delete=models.CASCADE,
                                     null=False, blank=False)
    wished_products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
