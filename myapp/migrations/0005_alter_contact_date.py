# Generated by Django 3.2.7 on 2021-11-25 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20211125_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 25, 13, 54, 11, 963168)),
        ),
    ]