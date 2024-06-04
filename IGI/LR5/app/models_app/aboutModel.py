from django.db import models
from app.models_app.basicModel import BasicModel


class About(BasicModel):
    text = models.TextField(help_text='Text about company')
    image = models.ImageField(blank=True, null=True,
                              upload_to='app/static/stock_images', help_text='Just friendly image')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        ordering = ['id']
        db_table = 'about_text'
