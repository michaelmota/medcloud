# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20161022_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='form_filled_by',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='refered_by',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]