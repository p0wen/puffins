from django.test import TestCase
from .forms import ContactForm


class TestContactView(TestCase):

    def test_get_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_page_uses_contact_form(self):
        response = self.client.get('/contact/')
        self.assertIsInstance(response.context['form'], ContactForm)
