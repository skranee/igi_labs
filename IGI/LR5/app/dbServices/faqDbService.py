from app.models_app.faqModel import Faq


class FaqDbService:
    @staticmethod
    def get_questions():
        return Faq.objects.all()