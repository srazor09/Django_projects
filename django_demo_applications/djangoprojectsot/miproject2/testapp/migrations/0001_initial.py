# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=64)),
                ('f2', models.CharField(max_length=64)),
                ('f3', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='StandardModel',
            fields=[
                ('basicmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.BasicModel')),
                ('f4', models.CharField(max_length=64)),
                ('f5', models.CharField(max_length=64)),
            ],
            bases=('testapp.basicmodel',),
        ),
    ]
