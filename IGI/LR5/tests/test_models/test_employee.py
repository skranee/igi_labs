from django.test import TestCase
from app.models_app.employeeModel import UserEmployee


class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserEmployee.objects.create(name='Test Employee', phone='+375291111111',
                                   email='test@employee.com', password='testpassword', isAdmin=True)

    def test_name_label(self):
        employee = UserEmployee.objects.get(id=1)
        field_label = employee._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_phone_label(self):
        employee = UserEmployee.objects.get(id=1)
        field_label = employee._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_email_label(self):
        employee = UserEmployee.objects.get(id=1)
        field_label = employee._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_password_label(self):
        employee = UserEmployee.objects.get(id=1)
        field_label = employee._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_name_max_length(self):
        employee = UserEmployee.objects.get(id=1)
        max_length = employee._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_phone_max_length(self):
        employee = UserEmployee.objects.get(id=1)
        max_length = employee._meta.get_field('phone').max_length
        self.assertEquals(max_length, 13)

    def test_password_max_length(self):
        employee = UserEmployee.objects.get(id=1)
        max_length = employee._meta.get_field('password').max_length
        self.assertEquals(max_length, 1500)