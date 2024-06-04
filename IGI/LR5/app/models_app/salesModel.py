from django.db import models
from app.models_app.basicModel import BasicModel
from app.models_app.productModel import Product
from app.models_app.customerModel import Customer


class Sales(BasicModel):
    products = models.ManyToManyField(Product, help_text='List of bought products')
    salePrice = models.IntegerField(default=0, help_text='Sale price')
    customer = models.ForeignKey(Customer, help_text='Customer that made a purchase',
                                 related_name='sales', on_delete=models.CASCADE)
    address = models.CharField(default='Minsk, Karbysheva 7', max_length=150, help_text='Address of the sale')

    def __str__(self):
        return f'{self.id} {self.createdAt} {self.lastUpdate} {self.salePrice} {self.products}'

    class Meta:
        ordering = ['createdAt']
        db_table = 'sales'
