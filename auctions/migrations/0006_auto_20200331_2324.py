# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-31 23:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200331_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 7, 23, 24, 40, 613744, tzinfo=utc), null=True),
        ),
    ]
