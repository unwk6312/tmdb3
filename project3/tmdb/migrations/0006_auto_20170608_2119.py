# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0005_auto_20170608_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='known',
            field=models.SlugField(default='', max_length=200),
        ),
    ]