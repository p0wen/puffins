from django.test import TestCase
from .models import FAQ


class TestFAQModel(TestCase):

    def test_return_self_title(self):
        question = FAQ.objects.create(category=1,
                                      name="return-policy",
                                      title="Whats the return policy?",
                                      answer="You have 30 days return")
        self.assertEqual(str(question), "Whats the return policy?")
