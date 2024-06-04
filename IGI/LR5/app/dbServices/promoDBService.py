from app.models_app.promoModel import Promo
from datetime import datetime


class PromoDbService:
    @staticmethod
    def get_promos():
        return Promo.objects.all()

    @staticmethod
    def check_existence(promo):
        check = Promo.objects.all().filter(code=promo).first()
        if check is None or check.valid_until < datetime.today().date():
            return False
        return True

    @staticmethod
    def get_discount(promo):
        return Promo.objects.all().filter(code=promo).first().discount
