from app.models_app.customerModel import Customer
from app.models_app.employeeModel import UserEmployee


class AuthDbService:
    @staticmethod
    def login(email: str):
        user = UserEmployee.objects.all().filter(email=email).first()
        if user is None:
            user = Customer.objects.all().filter(email=email).first()
            return user, 'user'
        return user, 'employee'

    @staticmethod
    def sign_up(email: str, name: str, phone: str, password: str):
        customer = Customer(email=email, name=name, phone=phone, password=password)
        customer.save()
        customer.refresh_from_db()
        return customer
