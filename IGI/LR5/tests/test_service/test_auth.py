from django.test import TestCase
from app.models_app.customerModel import Customer
from app.models_app.employeeModel import UserEmployee
from app.services.authService import AuthService
from app.security.security import *


class AuthServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(name='Test Customer', phone='+375291111111',
                                   email='test@customer.com', password=password_hash('testpassword'))
        UserEmployee.objects.create(name='Test Employee', phone='+375292222222',
                                   email='test@employee.com', password=password_hash('testpassword'), isAdmin=True)

    def test_sign_up(self):
        new_customer = AuthService.sign_up(
            'new@customer.com', 'New Customer', '+375293333333', 'newpassword')
        self.assertIsNotNone(new_customer)
        self.assertEquals(new_customer.name, 'New Customer')
        self.assertEquals(new_customer.phone, '+375293333333')
        self.assertEquals(new_customer.email, 'new@customer.com')
        self.assertTrue(password_verify('newpassword', new_customer.password))

    def test_sign_in_customer(self):
        user, role = AuthService.login('test@customer.com', 'testpassword')
        self.assertIsNotNone(user)
        self.assertEquals(role, 'user')
        self.assertEquals(user.name, 'Test Customer')
        self.assertEquals(user.phone, '+375291111111')
        self.assertEquals(user.email, 'test@customer.com')
        self.assertTrue(password_verify('testpassword', user.password))

    def test_sign_in_employee(self):
        user, role = AuthService.login('test@employee.com', 'testpassword')
        self.assertIsNotNone(user)
        self.assertEquals(role, 'admin')
        self.assertEquals(user.name, 'Test Employee')
        self.assertEquals(user.phone, '+375292222222')
        self.assertEquals(user.email, 'test@employee.com')
        self.assertTrue(password_verify('testpassword', user.password))
