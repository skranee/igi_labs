from django.db import models
from app.models_app.basicModel import BasicModel


class Category(BasicModel):
    name = models.CharField(max_length=100, help_text="Category name")

    def __str__(self):
        return f'{self.id} {self.createdAt} {self.lastUpdate} {self.name}'

    class Meta:
        db_table = 'categories'
        ordering = ['name']
