# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-12 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('dept', models.CharField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
    ]
