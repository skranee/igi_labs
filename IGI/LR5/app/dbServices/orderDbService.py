from app.models_app.orderModel import Order
from app.dbServices.customerDbService import CustomerDbService
from app.dbServices.productDbService import ProductDbService


class OrderDbService:

    @staticmethod
    def get_orders():
        return Order.objects.all()

    @staticmethod
    def get_orders_by_id(customer_id):
        return Order.objects.all().filter(customer=customer_id)

    @staticmethod
    def create_order(customer_id, product_id):
        customer = CustomerDbService.get_by_id(customer_id)
        product = ProductDbService.get_product_by_id(product_id)
        Order.objects.create(customer=customer, product=product)

    @staticmethod
    def delete_orders(orders):
        for order in orders:
            Order.objects.all().filter(id=order.id).delete()
