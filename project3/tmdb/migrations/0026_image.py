# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0025_auto_20170610_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(blank=True, default=0, null=True)),
                ('image', models.SlugField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
    ]
