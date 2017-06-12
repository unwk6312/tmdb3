# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import search_movie,movie 


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#     
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ['search_movie', 'movie_title', 'pub_date', 'movie_id', 'movie_overview']
#     class meta:
#         model = movie
#     
# 
# 
# class Movie(admin.StackedInline):
#     model = movie 
#   
# 
# 
# class SearchAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['total']}),
#        
#     ]
#    
#     inlines = [Movie]
# 
# admin.site.register(search_movie, SearchAdmin)
# 
# admin.site.register(movie, MovieAdmin)

