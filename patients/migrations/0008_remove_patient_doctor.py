# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 05:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_auto_20161116_0448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
    ]
