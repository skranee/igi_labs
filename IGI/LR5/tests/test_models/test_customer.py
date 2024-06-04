from django.test import TestCase
from app.models_app.customerModel import Customer


class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='testpassword')

    def test_name_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_phone_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_email_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_password_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_name_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_phone_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('phone').max_length
        self.assertEquals(max_length, 13)

    def test_password_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('password').max_length
        self.assertEquals(max_length, 1000)