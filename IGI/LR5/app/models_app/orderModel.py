from django.db import models
from app.models_app.basicModel import BasicModel
from app.models_app.productModel import Product
from app.models_app.customerModel import Customer


class Order(BasicModel):
    product = models.ForeignKey(Product, related_name='orders',
                                help_text='Product for the order', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='customers_order',
                                 help_text='Buyer', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.product} {self.customer}'

    class Meta:
        ordering = ['id']
        db_table = 'orders'
