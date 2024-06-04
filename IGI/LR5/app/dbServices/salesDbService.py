from app.models_app.salesModel import Sales
from app.dbServices.customerDbService import CustomerDbService


class SalesDbService:
    @staticmethod
    def get_sales():
        return Sales.objects.all()

    @staticmethod
    def create_sale(products, price, address, customer_id):
        ids = []
        for product in products:
            ids.append(product.id)
        customer = CustomerDbService.get_by_id(customer_id)
        sale = Sales.objects.create(salePrice=price, address=address, customer=customer)
        sale.products.set(ids)
        sale.save()
        return sale
