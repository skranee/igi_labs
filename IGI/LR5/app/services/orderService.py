from app.dbServices.orderDbService import OrderDbService


class OrderService:

    @staticmethod
    def get_orders():
        return OrderDbService.get_orders()

    @staticmethod
    def get_orders_by_id(customer_id):
        return OrderDbService.get_orders_by_id(customer_id)

    @staticmethod
    def create_order(customer_id, product_id):
        OrderDbService.create_order(customer_id, product_id)

    @staticmethod
    def delete_orders(orders):
        OrderDbService.delete_orders(orders)
