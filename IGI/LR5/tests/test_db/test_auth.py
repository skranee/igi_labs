from django.test import TestCase
from app.models_app.customerModel import Customer
from app.models_app.employeeModel import UserEmployee
from app.dbServices.auth_db_service import AuthDbService


class AuthRepositoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='Test Customer', phone='+375291111111',
                                   email='test@customer.com', password='testpassword')
        UserEmployee.objects.create(name='Test Employee', phone='+375292222222',
                                   email='test@employee.com', password='testpassword', isAdmin=True)

    def test_sign_up(self):
        new_customer = AuthDbService.sign_up(
            'new@customer.com', 'New Customer', '+375293333333', 'newpassword')
        self.assertIsNotNone(new_customer)
        self.assertEquals(new_customer.name, 'New Customer')
        self.assertEquals(new_customer.phone, '+375293333333')
        self.assertEquals(new_customer.email, 'new@customer.com')
        self.assertEquals(new_customer.password, 'newpassword')

    def test_sign_in_customer(self):
        user, role = AuthDbService.login('test@customer.com')
        self.assertIsNotNone(user)
        self.assertEquals(role, 'user')
        self.assertEquals(user.name, 'Test Customer')
        self.assertEquals(user.phone, '+375291111111')
        self.assertEquals(user.email, 'test@customer.com')
        self.assertEquals(user.password, 'testpassword')

    def test_sign_in_employee(self):
        user, role = AuthDbService.login('test@employee.com')
        self.assertIsNotNone(user)
        self.assertEquals(role, 'employee')
        self.assertEquals(user.name, 'Test Employee')
        self.assertEquals(user.phone, '+375292222222')
        self.assertEquals(user.email, 'test@employee.com')
        self.assertEquals(user.password, 'testpassword')