# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=100, unique=True, verbose_name='название актива')),
            ],
        ),
        migrations.CreateModel(
            name='AssetsBeneficiaris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share', models.DecimalField(blank=True, decimal_places=4, max_digits=6, verbose_name='доля бенефициара в активе, %')),
                ('rel_date', models.DateField(auto_now_add=True, verbose_name='дата актуальности')),
                ('source', models.CharField(max_length=40, verbose_name='источник')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Assets')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ben_name', models.CharField(max_length=20, verbose_name='имя')),
                ('ben_lastname', models.CharField(max_length=30, verbose_name='фамилия')),
                ('ben_midname', models.CharField(blank=True, max_length=30, verbose_name='отчество')),
                ('ben_holding', models.CharField(blank=True, max_length=70, verbose_name='холдинговая компания бенефициара')),
            ],
            options={
                'ordering': ['ben_lastname', 'ben_name'],
            },
        ),
        migrations.CreateModel(
            name='BeneficiaryOffshore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rel_date', models.DateField(auto_now_add=True, verbose_name='дата актуальности')),
                ('source', models.CharField(max_length=40, verbose_name='источник')),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Beneficiaries')),
            ],
        ),
        migrations.CreateModel(
            name='OffshoreAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share', models.DecimalField(blank=True, decimal_places=4, max_digits=6, verbose_name='доля бенефициара в активе, %')),
                ('rel_date', models.DateField(auto_now_add=True, verbose_name='дата актуальности')),
                ('source', models.CharField(max_length=40, verbose_name='источник')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Assets')),
            ],
        ),
        migrations.CreateModel(
            name='Offshores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('off_name', models.CharField(max_length=50, unique=True, verbose_name='название офшора')),
                ('off_jurisdiction', models.CharField(blank=True, max_length=50, verbose_name='юрисдикция офшора')),
                ('off_parent', models.CharField(blank=True, max_length=50, verbose_name='материнский офшор')),
            ],
        ),
        migrations.AddField(
            model_name='offshoreasset',
            name='offshore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Offshores'),
        ),
        migrations.AddField(
            model_name='beneficiaryoffshore',
            name='offshore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Offshores'),
        ),
        migrations.AlterUniqueTogether(
            name='beneficiaries',
            unique_together=set([('ben_name', 'ben_lastname', 'ben_midname')]),
        ),
        migrations.AddField(
            model_name='assetsbeneficiaris',
            name='beneficiary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Beneficiaries'),
        ),
    ]
