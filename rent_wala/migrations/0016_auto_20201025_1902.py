# Generated by Django 2.2.11 on 2020-10-26 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_wala', '0015_getorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='getorder',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]
