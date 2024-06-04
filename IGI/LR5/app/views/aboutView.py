from django.shortcuts import render
from app.services.aboutService import AboutService
from django.views import View
from django import forms
from app.models_app.aboutModel import About


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['text']


class AboutView(View):
    @staticmethod
    def get(request):
        about = AboutService.get_info()
        return render(request, "about.html", {'about': about})
