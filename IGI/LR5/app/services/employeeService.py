from app.dbServices.employee_db_service import EmployeeDbService


class EmployeeService:
    @staticmethod
    def get_all():
        return EmployeeDbService.get_all()

    @staticmethod
    def get_info_by_name(name: str):
        return EmployeeDbService.get_info_by_name(name)

    @staticmethod
    def get_by_id(id: int):
        return EmployeeDbService.get_by_id(id)

    @staticmethod
    def get_by_position(pos: str):
        return EmployeeDbService.get_by_position(pos)

    @staticmethod
    def get_by_email(email: str):
        return EmployeeDbService.get_by_email(email)
