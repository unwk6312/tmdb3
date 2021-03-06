# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0015_auto_20170609_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playing',
            name='image',
            field=models.SlugField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='playing',
            name='movie_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='playing',
            name='original_language',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='playing',
            name='overview',
            field=models.CharField(blank=True, default='', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='playing',
            name='release_date',
            field=models.DateTimeField(blank=True, default='', null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='playing',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='playing',
            name='vote_average',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
    ]
