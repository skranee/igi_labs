from django.db import models
from app.models_app.basicModel import BasicModel


class News(BasicModel):
    title = models.CharField(max_length=100, help_text="The title of the article")
    text = models.TextField(max_length=1500, help_text="The main text of the article")
    image = models.ImageField(upload_to='app/static/newsImages', help_text='The image for the article')

    def __str__(self):
        return f'{self.id} {self.createdAt} {self.lastUpdate} {self.title}'

    class Meta:
        db_table = 'news'
        ordering = ['createdAt']
