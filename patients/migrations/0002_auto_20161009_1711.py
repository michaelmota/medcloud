# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[(b'Hombre', b'Hombre'), (b'Mujer', b'Mujer')], max_length=10),
        ),
    ]
