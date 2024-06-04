from django.db import models
from app.models_app.basicModel import BasicModel


class Faq(BasicModel):
    title = models.CharField(max_length=100, help_text='The title of the question')
    text = models.TextField(help_text='The question itself')

    def __str__(self):
        return f'{self.id} {self.title}'

    class Meta:
        ordering = ['id']
        db_table = 'faq'
