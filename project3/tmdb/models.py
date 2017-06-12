# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.template.defaultfilters import default
class search_movie(models.Model):
    total=models.IntegerField(default=0)
    movie_text=models.CharField(max_length=200,default='')
     
    def __str__(self):
        return self.movie_text
#     class movie(models.Model):
 
class movie(models.Model):
    search_movie = models.ForeignKey('search_movie', null=True, blank=True, on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=200,default='')
    pub_date = models.DateTimeField('date published',null=True, blank=True)
    movie_id=models.IntegerField(default=0)
    movie_overview=models.CharField(max_length=200,default='',null=True, blank=True)
    
    
    
    
class movie_id(models.Model):
    movie_title=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',null=True, blank=True)
    overview=models.CharField(max_length=2000,null=True, blank=True)
    rating=models.FloatField(max_length=20,null=True, blank=True)
    movie_id=models.IntegerField(default=0)
    language=models.CharField(max_length=200,default='',null=True, blank=True)
    image=models.SlugField(max_length=200,default='',null=True, blank=True)
    trailer=models.SlugField(max_length=200,default='',null=True, blank=True)
    movie_original_title=models.CharField(max_length=200,default='',null=True, blank=True)
    

class character(models.Model):
    movie_id = models.ForeignKey('movie_id', on_delete=models.CASCADE,null=True, blank=True)
    movie_character=models.CharField(max_length=200,null=True, blank=True)
    movie_actor=models.CharField(max_length=200,null=True, blank=True)
    actor_id=models.IntegerField(default=0)
    
class review(models.Model):
    movie_id = models.ForeignKey('movie_id', on_delete=models.CASCADE)
    author=models.CharField(max_length=2000,default='',null=True, blank=True)
    movie_review=models.CharField(max_length=2000,default='None',null=True, blank=True)
    
class Search_name(models.Model):
    total=models.IntegerField(default=0)
    name_text=models.CharField(max_length=200,default='',null=True, blank=True)


class Name(models.Model):
    Search_name = models.ForeignKey('Search_name', on_delete=models.CASCADE,null=True, blank=True)

    name=models.CharField(max_length=200,default='',null=True, blank=True)
    known=models.SlugField(max_length=200,default='',null=True, blank=True)
    people_id=models.IntegerField(default=0,null=True, blank=True)

class People_detail(models.Model):
    name = models.CharField(max_length=200,default='',null=True, blank=True)
    gender=models.CharField(max_length=20,default='',null=True, blank=True)
    birthday = models.DateTimeField('date published',default='',null=True, blank=True)
    place_of_birth=models.CharField(max_length=200,default='',null=True, blank=True)
    biography = models.CharField(max_length=2000,default='',null=True, blank=True)
    image=models.SlugField(max_length=200,default='',null=True, blank=True)
    

class Known1(models.Model):
    People_detail = models.ForeignKey('People_detail', null=True, blank=True, on_delete=models.CASCADE)
    title=models.SlugField(max_length=200,default='',null=True, blank=True)
    movie_id=models.IntegerField(default=0)
    release_date=models.DateTimeField('date published',default='',null=True, blank=True)
    character=models.SlugField(max_length=200,default='',null=True, blank=True)
    
    
class Playing(models.Model):
    title = models.CharField(max_length=200,default='',null=True, blank=True)
    vote_average=models.FloatField(max_length=20,null=True, blank=True)
    
    original_language=models.CharField(max_length=20,default='',null=True, blank=True)
    overview=models.CharField(max_length=2000,default='',null=True, blank=True)
    release_date=models.DateTimeField('date published',default='',null=True, blank=True)
    movie_id=models.IntegerField(default=0,null=True, blank=True)
    image=models.SlugField(max_length=200,default='',null=True, blank=True)
    trailer=models.SlugField(max_length=200,default='',null=True, blank=True)
    
class Image(models.Model):
    movie_id=models.IntegerField(default=0,null=True, blank=True)
    image=models.SlugField(max_length=200,default='',null=True, blank=True)

    

    
    
    
    
    
    
    
    
    
    
