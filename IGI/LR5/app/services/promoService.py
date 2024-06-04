from app.dbServices.promoDBService import PromoDbService


class PromoService:
    @staticmethod
    def get_promos():
        return PromoDbService.get_promos()
