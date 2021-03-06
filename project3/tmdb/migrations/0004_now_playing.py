# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0003_auto_20170608_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Now_playing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('vote_average', models.FloatField(max_length=20)),
                ('poster_path', models.CharField(default='', max_length=200)),
                ('original_language', models.CharField(default='', max_length=20)),
                ('overview', models.CharField(default='', max_length=2000)),
                ('release_date', models.DateTimeField(default='', verbose_name='date published')),
                ('movie_id', models.IntegerField(default=0)),
            ],
        ),
    ]
