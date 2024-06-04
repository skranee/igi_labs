from django.test import TestCase
from app.views.promoView import PromoForm


class SaleCodeFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'code': 'code_10',
            'is_active': False,
        }

    def test_form_labels(self):
        form = PromoForm()
        self.assertEquals(form.fields['code'].label, 'Code')
        self.assertEquals(form.fields['archived'].label, 'Archived')

    def test_form_help_text(self):
        form = PromoForm()
        self.assertEquals(form.fields['code'].help_text, 'The code itself')
        self.assertEquals(form.fields['archived'].help_text, 'Archived or not')

    def test_form_invalid_code(self):
        self.form_data['code'] = 'code123'
        form = PromoForm(data=self.form_data)
        self.assertFalse(form.is_valid())

