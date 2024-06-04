from django.db import models
from app.models_app.basicModel import BasicModel


class UserEmployee(BasicModel):
    name = models.CharField(max_length=100, help_text='Name and surname')
    phone = models.CharField(max_length=13, unique=True, help_text='Phone number')
    email = models.EmailField(max_length=50, unique=True, help_text='Email address')
    password = models.CharField(max_length=1500, help_text='password')
    isAdmin = models.BooleanField(help_text='is admin')

    def __str__(self):
        return f'{self.id} {self.createdAt} {self.lastUpdate} {self.name} {self.phone} \
{self.email} {self.password} {self.isAdmin}'

    class Meta:
        ordering = ['name']
        db_table = 'employees_accounts'


class Employee(BasicModel):
    db_id = models.OneToOneField(UserEmployee, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, help_text='Position in company')
    salary = models.IntegerField(help_text='Monthly salary (gross)')
    photo = models.ImageField(upload_to='app/static/employees', help_text='Employee photo')

    def __str__(self):
        return f'{self.id} {self.createdAt} {self.lastUpdate} {self.db_id} {self.position} \
{self.salary} {self.photo}'

    class Meta:
        ordering = ['db_id']
        db_table = 'employees'
