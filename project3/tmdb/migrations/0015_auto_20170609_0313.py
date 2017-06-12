# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0014_people_detail_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playing',
            name='poster_path',
        ),
        migrations.AddField(
            model_name='playing',
            name='image',
            field=models.SlugField(default='', max_length=200),
        ),
    ]