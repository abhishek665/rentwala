# Generated by Django 2.2.11 on 2020-11-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_wala', '0017_auto_20201106_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.CharField(default='', max_length=500),
        ),
    ]
