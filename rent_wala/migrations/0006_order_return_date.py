# Generated by Django 2.2.11 on 2020-10-19 21:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rent_wala', '0005_order_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='return_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]