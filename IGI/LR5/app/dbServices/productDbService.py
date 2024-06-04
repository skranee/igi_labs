from app.models_app.productModel import Product
from app.models_app.supplierModel import Supplier
from app.models_app.categoryModel import Category
from collections import Counter
from app.models_app.salesModel import Sales


class ProductDbService:
    @staticmethod
    def get_products():
        return Product.objects.all()

    @staticmethod
    def get_most_popular():
        all_sales = Sales.objects.all()
        product_counter = Counter()
        for sale in all_sales:
            for product in sale.products.all():
                product_counter[product] += 1
        most_popular_product = product_counter.most_common(1)[0][0]

        return most_popular_product

    @staticmethod
    def get_product_by_id(product_id):
        return Product.objects.all().filter(id=product_id).first()

    @staticmethod
    def update(name, supplier_id, category_id, price, image, product_id):
        product = ProductDbService.get_product_by_id(product_id)
        product.image = 'app/static/products/' + image
        product.name = name
        product.price = price
        product.supplier = Supplier.objects.get(id=supplier_id)
        product.category = Category.objects.get(id=category_id)
        product.save()
        return product

    @staticmethod
    def delete(product_id):
        product = ProductDbService.get_product_by_id(product_id)
        product.delete()

    @staticmethod
    def create(name, supplier_id, category_id, price, image):
        supplier = Supplier.objects.get(id=supplier_id)
        category = Category.objects.get(id=category_id)
        product = Product.objects.create(name=name, supplier=supplier, category=category, price=price, image='app/static/products/' + image)
        product.save()
        return product
