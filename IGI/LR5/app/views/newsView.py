from app.models_app.newsModel import News
from django.shortcuts import render
from app.services.newsService import NewsService
from django.views import View
from django import forms


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['id', 'createdAt', 'lastUpdate']


class NewsView(View):
    @staticmethod
    def get(request):
        news = NewsService.get_news()
        return render(request, "news.html", {'news': news})
