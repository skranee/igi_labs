from app.dbServices.ratesDbService import RatesDbService


class RatesService:
    @staticmethod
    def get_rates():
        return RatesDbService.get_rates()

    @staticmethod
    def add_rate(text, customer_id, rate):
        return RatesDbService.add_rate(text, customer_id, rate)
