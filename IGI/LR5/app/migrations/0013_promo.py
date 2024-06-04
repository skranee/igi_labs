# Generated by Django 4.2.11 on 2024-05-12 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_rate_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(help_text='Unique ID', primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date')),
                ('lastUpdate', models.DateTimeField(default=django.utils.timezone.now, help_text='Update date')),
                ('value', models.CharField(help_text='Short description of the promo code', max_length=100)),
                ('valid_until', models.DateField(help_text='Valid until that date')),
                ('archived', models.BooleanField(help_text='Archived or not')),
            ],
            options={
                'db_table': 'promos',
                'ordering': ['id'],
            },
        ),
    ]
