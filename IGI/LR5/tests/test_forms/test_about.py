from django.test import TestCase
from app.views.aboutView import AboutForm


class AboutFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'info': 'Test info'
        }

    def test_form_help_text(self):
        form = AboutForm()
        self.assertEquals(form.fields['text'].help_text, 'Text about company')

    def test_form_invalid(self):
        self.form_data['text'] = ''
        form = AboutForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['text'], ['This field is required.'])
