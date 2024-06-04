from django.db import models
from django.utils import timezone


class BasicModel(models.Model):
    id = models.BigAutoField(primary_key=True, help_text='Unique ID')
    createdAt = models.DateTimeField(default=timezone.now, help_text='Creation date')
    lastUpdate = models.DateTimeField(default=timezone.now, help_text='Update date')

    class Meta:
        abstract = True
