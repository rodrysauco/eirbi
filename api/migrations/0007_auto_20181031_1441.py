# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20181031_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anfitrion',
            options={'verbose_name_plural': 'Anfitriones'},
        ),
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='fechaalq',
            options={'verbose_name_plural': 'FechasAlquiler'},
        ),
        migrations.AlterModelOptions(
            name='propiedad',
            options={'verbose_name_plural': 'Propiedades'},
        ),
        migrations.AddField(
            model_name='reserva',
            name='numeroReserva',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
