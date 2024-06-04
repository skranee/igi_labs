from django.test import TestCase
from app.views.newsView import NewsForm


class NewsFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'title': 'Test',
            'text': 'Test.',
            'image': None
        }

    def test_form_labels(self):
        form = NewsForm()
        self.assertEquals(form.fields['title'].label, 'Title')
        self.assertEquals(form.fields['text'].label, 'Text')
        self.assertEquals(form.fields['image'].label, 'Image')

    def test_form_help_text(self):
        form = NewsForm()
        self.assertEquals(form.fields['title'].help_text, 'The title of the article')
        self.assertEquals(form.fields['text'].help_text, 'The main text of the article')
        self.assertEquals(form.fields['image'].help_text, 'The image for the article')

    def test_form_invalid(self):
        self.form_data['title'] = ''
        form = NewsForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['title'], ['This field is required.'])
