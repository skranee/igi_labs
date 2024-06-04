from django.db import models
from app.models_app.basicModel import BasicModel
from app.models_app.customerModel import Customer
from django.core.validators import MinValueValidator, MaxValueValidator


class Rate(BasicModel):
    author = models.ForeignKey(Customer, related_name='rates',
                               help_text='The customer who left the rate', on_delete=models.CASCADE)
    text = models.TextField(help_text='The rate itself')
    rate = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)],
                            help_text='Rate from 1 to 10')

    def __str__(self):
        return f'{self.id} {self.createdAt} {self.author} {self.rate}'

    class Meta:
        ordering = ['id']
        db_table = 'rates'
