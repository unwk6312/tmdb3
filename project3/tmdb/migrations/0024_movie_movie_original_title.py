# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0023_movie_movie_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_original_title',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]