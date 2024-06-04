from app.dbServices.productDbService import ProductDbService


class ProductService:
    @staticmethod
    def get_products():
        return ProductDbService.get_products()

    @staticmethod
    def get_popular():
        return ProductDbService.get_most_popular()

    @staticmethod
    def get_product_by_id(product_id):
        return ProductDbService.get_product_by_id(product_id)

    @staticmethod
    def update(name, supplier_id, category_id, price, image, product_id):
        return ProductDbService.update(name, supplier_id, category_id, price, image, product_id)

    @staticmethod
    def delete(product_id):
        return ProductDbService.delete(product_id)

    @staticmethod
    def create(name, supplier_id, category_id, price, image):
        print(name)
        return ProductDbService.create(name, supplier_id, category_id, price, image)

