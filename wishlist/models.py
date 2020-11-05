from django.db import models
from products.models import Product
from useraccount.models import UserAccount


class UserWishlist(models.Model):
    user_profile = models.ForeignKey(UserAccount, on_delete=models.CASCADE,
                                     null=False, blank=False,
                                     related_name='wishlist')


class UserWishlistItem(models.Model):
    wishlist = models.ForeignKey(UserWishlist, null=False, blank=False, on_delete=models.CASCADE, related_name="wishitems")
    wished_products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'ProductID {self.product.name} on userwishlist {self.userwishlist.pk}'
