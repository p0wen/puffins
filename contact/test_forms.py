from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_first_name_required(self):
        form = ContactForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name']
                         [0], 'This field is required.')

    def test_fields_are_explicitin_inform_metaclass(self):
        form = ContactForm()
        self.assertEqual(form.Meta.fields, [
                         'first_name', 'last_name',
                         'email', 'category', 'message'])
