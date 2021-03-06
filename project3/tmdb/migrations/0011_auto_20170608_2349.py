# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0010_known_movie_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Known1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(default='', max_length=200)),
                ('movie_id', models.IntegerField(default=0)),
                ('release_date', models.DateTimeField(default='', verbose_name='date published')),
                ('character', models.CharField(default='', max_length=200)),
                ('People_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tmdb.People_detail')),
            ],
        ),
        migrations.RemoveField(
            model_name='known',
            name='People_detail',
        ),
        migrations.DeleteModel(
            name='Known',
        ),
    ]
