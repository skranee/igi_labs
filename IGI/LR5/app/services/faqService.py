from app.dbServices.faqDbService import FaqDbService


class FaqService:
    @staticmethod
    def get_questions():
        return FaqDbService.get_questions()
