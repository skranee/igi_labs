from app.models_app.vacancyModel import Vacancy


class VacanciesDbService:
    @staticmethod
    def get_vacancies():
        return Vacancy.objects.all()
