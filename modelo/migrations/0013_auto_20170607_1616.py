# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-07 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0012_auto_20170607_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='atendimento',
        ),
        migrations.AddField(
            model_name='atendimento',
            name='carrinho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modelo.Carrinho'),
        ),
        migrations.AlterField(
            model_name='carrinho',
            name='estoque',
            field=models.ManyToManyField(blank=True, null=True, to='modelo.Estoque'),
        ),
    ]
