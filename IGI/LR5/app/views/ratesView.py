from django.shortcuts import render, redirect
from django.views import View
from app.services.ratesService import RatesService
from django import forms
from app.models_app.rateModel import Rate


class RateForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        rate = cleaned_data.get('rate')
        if rate is not None:
            try:
                rate = int(rate)
                if 1 <= rate <= 10:
                    return cleaned_data
                else:
                    self.add_error('rate', 'Rate must be between 1 and 10')
            except ValueError:
                self.add_error('rate', 'Rate must be a valid integer')
        return cleaned_data

    class Meta:
        model = Rate
        fields = ['rate', 'text']


class RatesView(View):
    @staticmethod
    def get(request):
        rates = RatesService.get_rates()
        return render(request, "rates.html",
                      {'role': request.session['role'], 'rates': rates})

    @staticmethod
    def post(request):
        if(request.session['role'] == ''):
            return redirect('login')

        if(request.POST.get('rateBtn') and request.POST.get('rateBtn') == 'rate'):
            return render(request, "rates.html",
                          {'form': RateForm(), 'role': request.session['role']})
        form = RateForm(request.POST)
        if form.is_valid():
            save_rate = RatesService.add_rate(form.cleaned_data['text'],
                                              request.session['id'], form.cleaned_data['rate'])
            if save_rate is None:
                form.add_error(None, 'Some unpredicted error')
            else:
                return redirect('rates')
        return render(request, "rates.html",
                      {'role': request.session['role'], 'form': form, 'rates': RatesService.get_rates()})


