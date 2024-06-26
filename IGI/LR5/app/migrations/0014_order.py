# Generated by Django 4.2.11 on 2024-05-12 20:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_promo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(help_text='Unique ID', primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date')),
                ('lastUpdate', models.DateTimeField(default=django.utils.timezone.now, help_text='Update date')),
                ('customer', models.ForeignKey(help_text='Buyer', on_delete=django.db.models.deletion.CASCADE, related_name='customers_order', to='app.customer')),
                ('product', models.ForeignKey(help_text='Product for the order', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app.product')),
            ],
            options={
                'db_table': 'orders',
                'ordering': ['id'],
            },
        ),
    ]
