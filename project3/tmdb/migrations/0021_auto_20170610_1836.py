# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0020_auto_20170610_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
