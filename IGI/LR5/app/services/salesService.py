from app.dbServices.salesDbService import SalesDbService


class SalesService:
    @staticmethod
    def create_sale(products, price, address, customer_id):
        sale = SalesDbService.create_sale(products, price, address, customer_id)
        return sale
