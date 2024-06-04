from app.dbServices.vacanciesDbService import VacanciesDbService


class VacanciesService:
    @staticmethod
    def get_vacancies():
        return VacanciesDbService.get_vacancies()
