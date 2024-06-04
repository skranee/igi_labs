from django.test import TestCase
from app.views.authView import LoginForm, SignUpForm


class SignUpFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.form_data = {
            'name': 'Test User',
            'phone': '+375291111111',
            'email': 'test@test.com',
            'password': 'test123Test'
        }

    def test_form_phone_invalid(self):
        self.form_data['phone'] = '1234567890'
        form = SignUpForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(
            form.non_field_errors()[0], 'Phone must match the pattern: +37529XXXXXXX')


class LoginFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.form_data = {
            'email': 'test@test.com',
            'password': 'test123Test',
        }

    def test_form_labels(self):
        form = LoginForm()
        self.assertEquals(form.fields['email'].label, 'Email')
        self.assertEquals(form.fields['password'].label, 'Password')

    def test_form_hel_text(self):
        form = LoginForm()
        self.assertEquals(form.fields['email'].help_text, 'Email address')
        self.assertEquals(form.fields['password'].help_text, 'Password')

    def test_form_valid(self):
        form = LoginForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.form_data['password'] = ''
        form = LoginForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['password'], [
                          'This field is required.'])
