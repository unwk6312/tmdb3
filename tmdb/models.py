# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import default
from django.templatetags.i18n import language

# Create your models here.
class search_movie(models.Model):
    total=models.IntegerField(default=0)
    movie_text=models.CharField(max_length=200,default='')
     
    def __str__(self):
        return self.movie_text
#     class movie(models.Model):
 
class movie(models.Model):
    search_movie = models.ForeignKey('search_movie', on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    movie_id=models.IntegerField()
    movie_overview=models.CharField(max_length=2000,default='')
    
class movie_id(models.Model):
    movie_title=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    overview=models.CharField(max_length=2000)
    rating=models.FloatField(max_length=20)
    movie_id=models.IntegerField(default=0)
    language=models.CharField(max_length=200,default='')
    

class character(models.Model):
    movie_id = models.ForeignKey('movie_id', on_delete=models.CASCADE)
    movie_character=models.CharField(max_length=200)
    movie_actor=models.CharField(max_length=200)
    actor_id=models.IntegerField(default=0)
    
class review(models.Model):
    movie_id = models.ForeignKey('movie_id', on_delete=models.CASCADE)
    author=models.CharField(max_length=2000,default='')
    movie_review=models.CharField(max_length=2000,default='None')
    
    