# Generated by Django 2.2.11 on 2020-10-21 02:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rent_wala', '0012_auto_20201020_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneotp',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
