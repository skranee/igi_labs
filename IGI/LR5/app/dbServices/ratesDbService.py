from app.models_app.rateModel import Rate
from app.dbServices.customerDbService import CustomerDbService


class RatesDbService:
    @staticmethod
    def get_rates():
        return Rate.objects.all()

    @staticmethod
    def add_rate(text, customer_id, rate):
        user = CustomerDbService.get_by_id(customer_id)
        if user is None:
            return None
        else:
            rate = Rate.objects.create(text=text, author=user, rate=rate)
            rate.save()
            return rate
