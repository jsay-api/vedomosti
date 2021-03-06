# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_auto_20160721_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetsbeneficiaries',
            name='rel_date',
            field=models.DateField(auto_now_add=True, verbose_name='дата актуальности'),
        ),
        migrations.AlterField(
            model_name='beneficiariesoffshores',
            name='source',
            field=models.CharField(blank=True, max_length=40, verbose_name='источник'),
        ),
        migrations.AlterField(
            model_name='offshoresassets',
            name='source',
            field=models.CharField(blank=True, max_length=40, verbose_name='источник'),
        ),
    ]
