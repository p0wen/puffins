from django.test import TestCase
from django.contrib.auth.models import User
from .models import BlogPost
from useraccount.models import UserAccount


class TestContactView(TestCase):

    def setUp(self):
        password = 'mypassword'
        User.objects.create_superuser('myuser', 'myemail@test.com', password)
        self.client.login(username='myuser', password=password)

    def test_get_blog_overview(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_get_post(self):
        myuser = UserAccount.objects.get(user=1)
        BlogPost.objects.create(author=myuser,
                                title="Test-Post",
                                subtitle="Does this work?",
                                body="This is a post",)
        response = self.client.get('/blog/test-post')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/show_post.html')
