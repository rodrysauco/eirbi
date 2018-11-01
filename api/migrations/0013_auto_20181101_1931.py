# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_merge_20181101_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechaalq',
            name='reserva',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Reserva'),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='tarifaDiaria',
            field=models.IntegerField(),
        ),
    ]