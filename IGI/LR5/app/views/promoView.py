from django.views import View
from django.shortcuts import render
from app.services.promoService import PromoService
from app.models_app.promoModel import Promo
from django import forms


class PromoForm(forms.ModelForm):

    class Meta:
        model = Promo
        exclude = ['id', 'createdAt', 'lastUpdate']


class PromoView(View):
    @staticmethod
    def get(request):
        promos = PromoService.get_promos()
        return render(request, "promos.html",
                      {'role': request.session['role'], 'promos': promos})
