from app.models_app.basicModel import BasicModel
from app.models_app.categoryModel import Category
from app.models_app.supplierModel import Supplier
from django.db import models


class Product(BasicModel):
    name = models.CharField(max_length=200, help_text='Product name')
    supplier = models.ForeignKey(Supplier, help_text='Product supplier',
                                 related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=1,
                                 help_text='Product category',
                                 related_name='products_category', on_delete=models.CASCADE)
    price = models.IntegerField(help_text='Price for one product')
    image = models.ImageField(upload_to='app/static/products', help_text='Product image')

    def __str__(self):
        return f'{self.id} {self.createdAt} {self.lastUpdate} {self.name} {self.supplier} \
{self.price} '

    class Meta:
        ordering = ['price']
        db_table = 'products'
