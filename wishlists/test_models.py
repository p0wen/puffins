from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product, ProductLine, Category
from useraccount.models import UserAccount
from .models import UserWishlist


class TestUserWishlistModel(TestCase):

    def setUp(self):
        password = 'mypassword'
        User.objects.create_user('myuser', 'myemail@test.com', password)
        self.client.login(username='myuser', password=password)

    def test_wishlist_model(self):
        myuser = UserAccount.objects.get(user=1)
        wishlist_user = UserWishlist.objects.create(user_profile=myuser)
        category = Category.objects.create(name='kids', display_text='Kids')
        productline = ProductLine.objects.create(
            name='tshirt', display_text='T-Shirts')
        product = Product.objects.create(category=category,
                                         productline=productline,
                                         name="lovely",
                                         display_text="Lovely Puffin",
                                         price="49.99", discount_price=45.00)
        product.userwishlists.add(wishlist_user.id)
        wishlist = UserWishlist.objects.get(user_profile=myuser)
        self.assertEqual(str(wishlist), "myuser Wishlist")
