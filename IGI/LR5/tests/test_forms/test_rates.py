from django.test import TestCase
from app.views.ratesView import RateForm


class ReviewFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'rate': 3,
            'text': 'text',
        }

    def test_form_labels(self):
        form = RateForm()
        self.assertEquals(form.fields['rate'].label, 'Rate')
        self.assertEquals(form.fields['text'].label, 'Text')

    def test_form_help_text(self):
        form = RateForm()
        self.assertEquals(form.fields['rate'].help_text, 'Rate from 1 to 10')
        self.assertEquals(form.fields['text'].help_text, 'The rate itself')

    def test_form_valid(self):
        form = RateForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)

    def test_form_invalid(self):
        self.form_data['text'] = ''
        form = RateForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['text'], ['This field is required.'])

    def test_form_invalid_rate(self):
        self.form_data['rate'] = 15
        form = RateForm(data=self.form_data)
        self.assertFalse(form.is_valid())
