# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0021_auto_20170610_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_id',
            field=models.IntegerField(default=0),
        ),
    ]