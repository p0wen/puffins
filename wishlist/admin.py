from django.contrib import admin
from .models import UserWishlist, UserWishlistItem


class UserWishlistItemAdmin(admin.TabularInline):
    model = UserWishlistItem


class UserWishlistAdmin(admin.ModelAdmin):
    inlines = (UserWishlistItemAdmin,)

    list_display = (
        'user_profile',
        'wished_products',
        )


admin.site.register(UserWishlist)
admin.site.register(UserWishlistItem)
