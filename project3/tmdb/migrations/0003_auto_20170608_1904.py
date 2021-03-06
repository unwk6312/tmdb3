# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0002_auto_20170606_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('known', models.CharField(default='', max_length=200)),
                ('people_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='People_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('gender', models.CharField(default='', max_length=20)),
                ('birthday', models.DateTimeField(default='', verbose_name='date published')),
                ('place_of_birth', models.CharField(default='', max_length=200)),
                ('biography', models.CharField(default='', max_length=2000)),
                ('people_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Search_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('name_text', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='name',
            name='Search_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmdb.Search_name'),
        ),
    ]
