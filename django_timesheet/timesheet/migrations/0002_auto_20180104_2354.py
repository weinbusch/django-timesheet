# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-04 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='reference',
            field=models.CharField(max_length=128, unique=True, verbose_name='Aktenzeichen'),
        ),
    ]
