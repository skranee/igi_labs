from django.test import TestCase
from app.models_app.employeeModel import UserEmployee, Employee
from app.dbServices.employee_db_service import EmployeeDbService


class EmployeeRepositoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        employee = UserEmployee.objects.create(
            name='Test Employee', phone='+375291111111', email='test@employee.com', password='testpassword', isAdmin=True)
        UserEmployee.objects.create(name='Manager', phone='+375292222222',
                                   email='test1@employee.com', password='testpassword', isAdmin=False)
        Employee.objects.create(
            db_id=employee, salary=4000, position='This is a test description', photo='/img.png')

    def test_get_by_id(self):
        empl = EmployeeDbService.get_by_id(1)
        self.assertIsNotNone(empl)
        self.assertEquals(empl.name, 'Test Employee')
        self.assertEquals(empl.phone, '+375291111111')
        self.assertEquals(empl.email, 'test@employee.com')
        self.assertEquals(empl.password, 'testpassword')
