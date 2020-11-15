from django.test import TestCase
from django.contrib.auth.models import User
from useraccount.models import UserAccount


class TestUserAccountModel(TestCase):

    def test_str_method_for_useraccount(self):
        password = 'mypassword'
        User.objects.create_user('myuser', 'myemail@test.com', password)
        self.client.login(username='myuser', password=password)
        myuser = UserAccount.objects.get(user=1)
        self.assertEqual(str(myuser), "myuser")
