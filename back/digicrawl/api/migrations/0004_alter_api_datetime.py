# Generated by Django 3.2.7 on 2022-01-02 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_api_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 17, 35, 19, 511595)),
        ),
    ]
