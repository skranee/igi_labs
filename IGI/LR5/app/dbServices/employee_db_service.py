from app.models_app.employeeModel import Employee, UserEmployee


class EmployeeDbService:
    @staticmethod
    def get_all():
        return Employee.objects.all()

    @staticmethod
    def get_info_by_name(name: str):
        try:
            return UserEmployee.objects.all().filter(name=name).first()
        except:
            return None

    @staticmethod
    def get_by_id(id: int):
        try:
            return UserEmployee.objects.all().filter(id=id).first()
        except:
            return None

    @staticmethod
    def get_by_position(pos: str):
        try:
            return Employee.objects.all().filter(position=pos)
        except:
            return None

    @staticmethod
    def get_by_email(email: str):
        try:
            return Employee.objects.all().filter(email=email).first()
        except:
            return None
