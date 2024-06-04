from app.models_app.newsModel import News


class NewsService:
    @staticmethod
    def get_last_news():
        return News.objects.all().last()

    @staticmethod
    def get_news():
        return News.objects.all()
