from django.views import View
from django.shortcuts import render
from app.services.faqService import FaqService
from django import forms
from app.models_app.faqModel import Faq


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        exclude = ['id', 'createdAt', 'lastUpdate']


class FaqView(View):
    @staticmethod
    def get(request):
        questions = FaqService.get_questions()
        return render(request, 'faq.html', {'questions': questions})
