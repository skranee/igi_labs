# Generated by Django 4.2.11 on 2024-05-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(help_text='The image for the article', upload_to='app/static/newsImages'),
        ),
    ]
