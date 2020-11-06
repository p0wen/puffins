from django.contrib import admin
from .models import UserWishlist


class UserWishlistAdmin(admin.ModelAdmin):

    list_display = (
        'user_profile',
        'wished_products',
        )


admin.site.register(UserWishlist)
