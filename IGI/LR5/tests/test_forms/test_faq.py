from django.test import TestCase
from app.views.faqView import FaqForm


class QAFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'title': 'WUT?',
            'text': 'YES',
        }

    def test_form_labels(self):
        form = FaqForm()
        self.assertEquals(form.fields['title'].label, 'Title')
        self.assertEquals(form.fields['text'].label, 'Text')

    def test_form_help_text(self):
        form = FaqForm()
        self.assertEquals(form.fields['title'].help_text, 'The title of the question')
        self.assertEquals(form.fields['text'].help_text, 'The question itself')

    def test_form_valid(self):
        form = FaqForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)
