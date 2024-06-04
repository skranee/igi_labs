from django.test import TestCase
from app.views.productView import ProductDetailForm


class ProductFormTest(TestCase):
    def test_form_labels(self):
        form = ProductDetailForm()
        self.assertEquals(form.fields['name'].label, 'name')
        self.assertEquals(form.fields['price'].label, 'price')
        self.assertEquals(form.fields['category'].label, 'category')
        self.assertEquals(form.fields['image'].label, 'image')
        self.assertEquals(form.fields['supplier'].label, 'supplier')

    def test_form_help_text(self):
        form = ProductDetailForm()
        self.assertEquals(form.fields['name'].help_text, 'Product name')
        self.assertEquals(form.fields['price'].help_text, 'Price for one product')
        self.assertEquals(
            form.fields['category'].help_text, 'Product category')
        self.assertEquals(form.fields['image'].help_text, 'Product image')
        self.assertEquals(form.fields['supplier'].help_text, 'Product supplier')

    def test_form_valid(self):
        form = ProductDetailForm(data=self.form_data)
        self.assertTrue(form.is_valid())
