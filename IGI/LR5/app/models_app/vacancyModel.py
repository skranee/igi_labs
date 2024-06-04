from django.db import models
from app.models_app.basicModel import BasicModel


class Vacancy(BasicModel):
    position = models.CharField(max_length=100, help_text='The name of the position')
    description = models.TextField(help_text='The description of the job')
    salary = models.IntegerField(help_text='Monthly salary (gross)')

    def __str__(self):
        return f'{self.id} {self.salary} {self.position}'

    class Meta:
        ordering = ['salary']
        db_table = 'vacancies'
