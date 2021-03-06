# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cita',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='cita',
            name='doctor',
            field=models.CharField(choices=[(b'', b'-- Seleccionar --'), (b'Raul Rodriguez', b'Raul Rodriguez'), (b'El Viejo', b'El Viejo')], max_length=30),
        ),
        migrations.AlterField(
            model_name='cita',
            name='insurance',
            field=models.CharField(choices=[(b'', b'-- Seleccionar --'), (b'ARS Humano', b'ARS Humano'), (b'ARS Palic', b'ARS Palic'), (b'Universal', b'Universal'), (b'SeNaSa', b'SeNaSa'), (b'Seguros Banreservas', b'Seguros Banreservas')], max_length=40),
        ),
        migrations.AlterField(
            model_name='cita',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nombre_paciente', to='patients.Patient'),
        ),
    ]
