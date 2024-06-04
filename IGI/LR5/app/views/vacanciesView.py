from django.shortcuts import render
from django.views import View
from app.services.vacanciesService import VacanciesService


class VacanciesView(View):
    @staticmethod
    def get(request):
        positions = VacanciesService.get_vacancies()
        return render(request, "vacancies.html",
                      {'role': request.session['role'], 'positions': positions})
