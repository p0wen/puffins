from django.test import TestCase
from django.contrib.auth.models import User
from .models import BlogPost
from useraccount.models import UserAccount


class TestBlogPost(TestCase):

    def setUp(self):
        password = 'mypassword'
        User.objects.create_superuser('myuser', 'myemail@test.com', password)
        self.client.login(username='myuser', password=password)

    def test_return_self_title(self):
        myuser = UserAccount.objects.get(user=1)
        post = BlogPost.objects.create(author=myuser,
                                       title="Test-Post",
                                       subtitle="Does this work?",
                                       body="This is a post",)
        self.assertEqual(str(post), "Test-Post")

    def test_set_slug_title(self):
        myuser = UserAccount.objects.get(user=1)
        post_1 = BlogPost.objects.create(author=myuser,
                                         title="Test-Post",
                                         subtitle="Does this work?",
                                         body="This is a post",)
        post_2 = BlogPost.objects.create(author=myuser,
                                         title="Test-Post",
                                         subtitle="Does this work?",
                                         body="This is a post",)
        self.assertEqual(post_1.slug, "test-post")
        self.assertEqual(post_2.slug, "test-post-1")
