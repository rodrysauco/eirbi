# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 23:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20181109_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='fechaDeReservaFin',
            new_name='fechaRealizada',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='fechaDeReservaInicio',
        ),
    ]
