from app.models_app.employeeModel import Employee


class ContactsDbService:
    @staticmethod
    def get_employees():
        return Employee.objects.all()
