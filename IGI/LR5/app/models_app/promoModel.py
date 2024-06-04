from django.db import models
from app.models_app.basicModel import BasicModel


class Promo(BasicModel):
    value = models.CharField(max_length=100, help_text='Short description of the promo code')
    valid_until = models.DateField(help_text='Valid until that date')
    archived = models.BooleanField(help_text='Archived or not')
    code = models.CharField(max_length=20, default='ZooZoo', help_text='The code itself')
    discount = models.IntegerField(default=0, help_text='Discount of the promo')

    def __str__(self):
        return f'{self.id} {self.value} {self.discount}'

    class Meta:
        ordering = ['id']
        db_table = 'promos'
