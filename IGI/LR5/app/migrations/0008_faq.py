# Generated by Django 4.2.11 on 2024-05-10 22:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(help_text='Unique ID', primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date')),
                ('lastUpdate', models.DateTimeField(default=django.utils.timezone.now, help_text='Update date')),
                ('title', models.CharField(help_text='The title of the question', max_length=100)),
                ('text', models.TextField(help_text='The question itself')),
            ],
            options={
                'db_table': 'faq',
                'ordering': ['id'],
            },
        ),
    ]
