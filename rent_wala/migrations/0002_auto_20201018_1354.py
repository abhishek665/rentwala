# Generated by Django 2.2.11 on 2020-10-18 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_wala', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackorder',
            name='order_name',
            field=models.CharField(blank=True, max_length=10000000000),
        ),
        migrations.AddField(
            model_name='trackorder',
            name='order_qty',
            field=models.CharField(blank=True, max_length=10000000000),
        ),
        migrations.AddField(
            model_name='trackorder',
            name='order_total',
            field=models.CharField(blank=True, max_length=10000000000),
        ),
        migrations.AddField(
            model_name='trackorder',
            name='time_left',
            field=models.CharField(blank=True, max_length=10000000000),
        ),
        migrations.AddField(
            model_name='trackorder',
            name='total_days',
            field=models.CharField(blank=True, max_length=10000000000),
        ),
    ]
