# Generated by Django 2.2.11 on 2020-10-19 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_wala', '0006_order_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='return_date',
            field=models.DateTimeField(),
        ),
    ]
