from django.db import models
from app.models_app.basicModel import BasicModel


class Customer(BasicModel):
    email = models.EmailField(max_length=50, unique=True, help_text='Email address')
    name = models.CharField(max_length=100, help_text='Name and surname')
    phone = models.CharField(max_length=13, unique=True, help_text='Phone number')
    password = models.CharField(max_length=1000, help_text='Password')

    def __str(self):
        return f'{self.name} {self.email}'

    class Meta:
        ordering = ['name']
        db_table = 'customers'


class RegularCustomer(BasicModel):
    customer = models.ForeignKey(Customer, help_text='Customer related',
                                 related_name='regular', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.createdAt} {self.lastUpdate} {self.customer}'

    class Meta:
        ordering = ['createdAt']
        db_table = 'regular_customers'
