# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20181031_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
