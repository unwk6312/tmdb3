# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0026_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='Search_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tmdb.Search_name'),
        ),
    ]
