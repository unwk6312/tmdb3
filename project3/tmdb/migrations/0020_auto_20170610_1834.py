# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0019_auto_20170610_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_overview',
        ),
        migrations.AlterField(
            model_name='character',
            name='movie_actor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='movie_character',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='movie_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tmdb.movie_id'),
        ),
        migrations.AlterField(
            model_name='known1',
            name='character',
            field=models.SlugField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='known1',
            name='title',
            field=models.SlugField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='movie_id',
            name='image',
            field=models.SlugField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie_id',
            name='language',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie_id',
            name='overview',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='movie_id',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='movie_id',
            name='rating',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='name',
            name='known',
            field=models.SlugField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='name',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='name',
            name='people_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='people_detail',
            name='biography',
            field=models.CharField(blank=True, default='', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='people_detail',
            name='birthday',
            field=models.DateTimeField(blank=True, default='', null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='people_detail',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='people_detail',
            name='image',
            field=models.SlugField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='people_detail',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='people_detail',
            name='place_of_birth',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(blank=True, default='', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie_review',
            field=models.CharField(blank=True, default='None', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='search_name',
            name='name_text',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]