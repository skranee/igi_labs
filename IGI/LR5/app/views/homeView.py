from django.shortcuts import render
from app.security.security import check_auth
from app.services.outerApiService import OuterApiService
from app.services.newsService import NewsService


def get_last_news():
    article = NewsService.get_last_news()
    return article


def home(request):
    check_auth(request.session)
    article = get_last_news()
    return render(request, "home.html", {'role': request.session['role'],
                                         'article': article})
