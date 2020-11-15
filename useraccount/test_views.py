from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserAccount
from .forms import UserAccountForm


class TestUserAccountView(TestCase):

    def test_get_useraccount_page_success(self):
        password = 'mypassword'
        User.objects.create_user('myuser', 'myemail@test.com', password)
        self.client.login(username='myuser', password=password)
        response = self.client.get('/useraccount/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'useraccount/profile.html')

    def test_get_useraccount_page_fail(self):
        response = self.client.get('/useraccount/')
        self.assertTrue(response.status_code, 500)
