from django.test import TestCase


class TestContactView(TestCase):

    def test_get_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
