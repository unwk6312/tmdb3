# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import  search_movie,movie,movie_id
from django.http import HttpResponse
import requests 
from django.templatetags.i18n import language
def get_charactors(id):
    id=str(id)
    url='https://api.themoviedb.org/3/movie/'+id+'/credits?api_key=1c7b5989619b35104b3713869fdd3ca9'
    payload = "{}"
    response = requests.request("GET", url, data=payload,verify=False)
    result=response.json()
    #print len(result['cast'])
    d=dict()
    for i in result['cast']:
       d[i['cast_id']]=d.get(i['cast_id'],(i['character'],i['name'],i['id']))
    t=d.items()
    t.sort()
    for i in result['crew']:
        if i['job']=='Director':
          director=(i['job'],i['name'],i['id'])
 
    
    return director,t 
def get_reviwer(id):
    id=str(id)
    url='https://api.themoviedb.org/3/movie/'+id+'/reviews?api_key=1c7b5989619b35104b3713869fdd3ca9'

    payload = "{}"
    response = requests.request("GET", url, data=payload,verify=False)
    result=response.json()
    
    d={}
    for i in result['results']:
        
        d[i['author']]=d.get(i['author'],i['content'])
    return d 

def search(request,name):
     url = 'https://api.themoviedb.org/3/search/movie?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US&query=%E2%80%99'+name+'%E2%80%98&page=1&include_adult=false'
     payload = "{}"
     response = requests.request("GET", url, data=payload,verify=False)
     result=response.json()
     a=search_movie(total=result['total_results'],movie_text=name)
     a.save()
     for i in result['results']:
         a.movie_set.create(movie_title=i['title'],pub_date=i['release_date'] ,movie_id=i['id'],movie_overview=i['overview'])
            

     return render(request, 'tmdb/search.html', {'a': a})
def details(request,id): 
    id=str(id) 
    url = "https://api.themoviedb.org/3/movie/"+id+"?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US"
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    result=response.json()
    
    b=movie_id(movie_title=result["original_title"],pub_date =result["release_date"],overview=result["overview"], rating=result["vote_average"],language=result["original_language"],movie_id=id)
    b.save()
    c=get_charactors(b.movie_id)
    b.character_set.create(movie_character=c[0][0],movie_actor=c[0][1],actor_id=c[0][2])
    for i in c[1]:
        b.character_set.create(movie_character=i[1][0],movie_actor=i[1][1],actor_id=i[1][2])
    d=get_reviwer(b.movie_id)
    if d!={}:
        for i in d:
         b.review_set.create(author=i,movie_review=d[i])
        
    
    
    return render(request, 'tmdb/details.html', {'b': b})
#   return HttpResponse("Hello, world. You're at the polls index.")





    
    
    
    
