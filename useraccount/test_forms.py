from django.test import TestCase
from .forms import MyCustomSignupForm, UserAccountForm


class TestExtendSignupForm(TestCase):

    def test_first_name_required(self):
        form = MyCustomSignupForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name']
                         [0], 'This field is required.')

    def test_extended_signup_form(self):
        form = MyCustomSignupForm({
            'email': 'test@test.io',
            'email2': 'test@test.io',
            'first_name': 'test',
            'last_name': 'user',
            'password1': '312jcs13das',
            'password2': '312jcs13das',
        })
        self.assertTrue(form.is_valid())


class TestUserAccountForm(TestCase):

    def test_fields_are_explicitin_inform_metaclass(self):
        form = UserAccountForm()
        self.assertEqual(form.Meta.exclude, ('user',))
