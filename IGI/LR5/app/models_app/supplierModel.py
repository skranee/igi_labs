from app.models_app.basicModel import BasicModel
from django.db import models


class Supplier(BasicModel):
    country = models.CharField(max_length=50, help_text='Country of the company')
    name = models.CharField(max_length=100, help_text='Company name')
    deliveryTime = models.IntegerField(help_text='Days of delivery')
    foundationDate = models.DateField(help_text='Foundation date')

    def __str__(self):
        return f'{self.id} {self.createdAt} {self.lastUpdate} {self.country} \
{self.deliveryTime} {self.foundationDate} {self.name}'

    class Meta:
        db_table = 'suppliers'
        ordering = ['country']
