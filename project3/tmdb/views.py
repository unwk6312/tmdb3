# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
from .models import  search_movie,movie,movie_id,Search_name, Name, People_detail,review,character,Playing,Known1,Image
from django.http import HttpResponse
import requests 
import datetime
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from mhlib import PATH
DEVELOPER_KEY = "AIzaSyBy7vm2GZrsUjQnR76ardJfgPquaf7NEdw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def exit_or_not(a,b):
    if a in b.keys() and b[a]!=None:
            c=b[a]
    else:
            c=None
    return c 

def get_trailer(a):
    l=[]
    a=str(a)+' trailer'
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
    
    search_response = youtube.search().list(
    q=a ,
    part="id,snippet",
    
    ).execute()
    for i in search_response['items']:
        if 'id' in i.keys():
            if 'videoId' in i['id'].keys():
                l.append(i['id']['videoId'])
                break
    if l!=[]:
        return str(l[0])
    else:
        return None
    
    
def get_known(id):
    id=str(id)
    url="https://api.themoviedb.org/3/person/"+id+"/movie_credits?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US"
    payload = "{}"
    response = requests.request("GET", url, data=payload,verify=False)
    result=response.json()
    return result

def get_charactors(id):
    id=str(id)
    url='https://api.themoviedb.org/3/movie/'+id+'/credits?api_key=1c7b5989619b35104b3713869fdd3ca9'
    payload = "{}"
    response = requests.request("GET", url, data=payload,verify=False)
    result=response.json()
    d=dict()
    for i in result['cast']:
       d[i['cast_id']]=d.get(i['cast_id'],(i['character'],i['name'],i['id']))
    t=d.items()
    t.sort()
    if result['crew']!=[]:
        for i in result['crew']:
            if i['job']=='Director':
                director=(i['job'],i['name'],i['id'])
    else:
        director=None
 
    
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
     name=str(name)
     url = 'https://api.themoviedb.org/3/search/movie?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US&query=%E2%80%99'+name+'%E2%80%98&page=1&include_adult=false'
     payload = "{}"
     response = requests.request("GET", url, data=payload,verify=False)
     result=response.json()
     a=search_movie(total=result['total_results'],movie_text=name)
     a.save()
     for i in result['results']:
        if i['release_date'] != "":
            print type(i['release_date']), i['release_date']
            a.movie_set.create(movie_title=i['title'],pub_date=i['release_date'] ,movie_id=i['id'],movie_overview=i['overview'])
     return render(request, 'tmdb/search.html', {'a': a})
def details(request,id): 
    id=str(id) 
    url = "https://api.themoviedb.org/3/movie/"+id+"?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US"
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    result=response.json()
    if result['poster_path']==None:
        poster="tmdb/images/n.jpg"
    else:
        poster='https://image.tmdb.org/t/p/w185'+result['poster_path']
    path=get_trailer(result["title"])
    if path!=None:
        path='https://www.youtube.com/watch?v='+path 
    
    b=movie_id(movie_original_title=result["original_title"],movie_title=result["title"],pub_date =result["release_date"],overview=result["overview"], rating=result["vote_average"],language=result["original_language"],movie_id=id,image=poster,trailer=path)
    b.save()

    c=get_charactors(b.movie_id)
    if c[0]!=None:
        b.character_set.create(movie_character=c[0][0],movie_actor=c[0][1],actor_id=c[0][2])
    for i in c[1]:
        b.character_set.create(movie_character=i[1][0],movie_actor=i[1][1],actor_id=i[1][2])
    d=get_reviwer(b.movie_id)
    if d!={}:
        for i in d:
         b.review_set.create(author=i,movie_review=d[i])
        

    return render(request, 'tmdb/details.html', {'b': b})

def index(request):
        url='https://api.themoviedb.org/3/movie/upcoming?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US&page=1'
        payload = "{}"
        response = requests.request("GET", url, data=payload,verify=False)
        result=response.json()
        d=dict()
        b=datetime.datetime.now()
      
        diff=datetime.timedelta(days=1)
        for i in result['results']:
            a=datetime.datetime.strptime(i['release_date'],'%Y-%m-%d')
            if (a-b)>diff:
                if i['backdrop_path']==None:
                    poster="tmdb/images/n.jpg"
                else:
                    poster='https://image.tmdb.org/t/p/w1280'+i['backdrop_path']
              
                d[i['release_date']]=d.get(i['release_date'],(poster,i['id']))
       
        l=d.keys()
        l.sort()
        k=[]
        for i in l :
            
            a = Image(image=d[i][0],movie_id=d[i][1])
            a.save()
            k.append(a)
        return render(request, 'tmdb/index.html', {'k': k})


def search1(request, name):
    url = 'https://api.themoviedb.org/3/search/person?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US&query=' + name + '&page=1&include_adult=false'
    payload = "{}"
    response = requests.request("GET", url, data=payload, verify=False)
    result = response.json()
    e = ''
    f = 0 
    a = Search_name(total=result['total_results'], name_text=name)
    a.save()
    for i in result['results']:
       
        for k in i['known_for']:

            if 'title'in k.keys():
                 e = e + k['title']+','
            elif'original_name' in k.keys():
                e = e + k['original_name']+','
            else:
                e=e 
     
        e=e[:-1]
        a.name_set.create(name=i['name'],known=e,people_id=i['id'])

    return render(request, 'tmdb/peoples.html', {'a': a})

def search2(request, id):
    id = str(id)
 
    url='https://api.themoviedb.org/3/person/'+id+'?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US'

    payload = "{}"
    
    response = requests.request("GET", url, data=payload, verify=False)
    result = response.json()
   
    if result["gender"]==1:
        c='female'
    else:
        c='male'

    if result['profile_path']==None:
            poster="tmdb/images/n.jpg"
    else:
            poster='https://image.tmdb.org/t/p/w185'+result['profile_path']
    
    if result["birthday"]!=None:
        if len(result["birthday"])!=10:
            result["birthday"]=None
        

    b = People_detail(name=result["name"], gender=c,birthday=result["birthday"], biography=result["biography"],
                      place_of_birth=result["place_of_birth"],image=poster)
    b.save()
   
    knowing=get_known(result['id'])
    if 'cast' in knowing.keys():
        for i in knowing['cast']:

                b.known1_set.create(title=i["title"],movie_id=i["id"],release_date=i["release_date"],character=i["character"])
    if "crew" in knowing.keys():
        print 'jdjhsjfhs'
        for i in knowing['crew']:

                b.known1_set.create(title=i["title"],movie_id=i["id"],release_date=i["release_date"],character=i['department'])
                
        
    return render(request, 'tmdb/bio.html', {'b': b})

def playing(request):
    url='https://api.themoviedb.org/3/movie/now_playing?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US&page=1'
    payload = "{}"
    response = requests.request("GET", url, data=payload,verify=False)
    result=response.json()
    l=[]
    k=[]
    for i in result['results']:
        if i['poster_path']==None:
            poster="tmdb/images/n.jpg"
        else:
            poster='https://image.tmdb.org/t/p/w185'+i['poster_path']
        path=get_trailer(i['title'])
        if path!=None:
            path='https://www.youtube.com/watch?v='+path 
     
        a=(i['release_date'],i['id'],i['title'],i['vote_average'],poster,i['original_language'],i['overview'],path)
        l.append(a)
        l.sort(reverse=True)
  
    for i in range (10):
    
        
        a = Playing(title=l[i][2],image=l[i][4],original_language=l[i][5],overview=l[i][6],release_date=l[i][0],movie_id=l[i][1],vote_average=l[i][3],trailer=l[i][7])
        a.save()
        k.append(a)
   
    return render(request, 'tmdb/news.html', {'k': k})

def upcoming(request):
    url='https://api.themoviedb.org/3/movie/upcoming?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US&page=1'
    payload = "{}"
    response = requests.request("GET", url, data=payload,verify=False)
    result=response.json()
    d=dict()
    b=datetime.datetime.now()
    diff=datetime.timedelta(days=1)
    for i in result['results']:
            a=datetime.datetime.strptime(i['release_date'],'%Y-%m-%d')
            if (a-b)>diff:
                if i['poster_path']==None:
                    poster="tmdb/images/n.jpg"
                else:
                    poster='https://image.tmdb.org/t/p/w185'+i['poster_path']
                path=get_trailer(i['title'])
                if path!=None:
                    path='https://www.youtube.com/watch?v='+path 
                    
                 
              
                d[i['release_date']]=d.get(i['release_date'],(poster,i['title'],i['overview'],i['vote_average'],i['id'],i['original_language'],path))
    l=d.keys()
    l.sort()
    k=[]
    for i in l :
    
        a = Playing(title=d[i][1],image=d[i][0],original_language=d[i][5],overview=d[i][2],release_date=i,movie_id=d[i][4],vote_average=d[i][3],trailer=d[i][6])
        a.save()
     
        k.append(a)
    return render(request, 'tmdb/coming.html', {'k': k})

def popular(request):
    url='https://api.themoviedb.org/3/movie/popular?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US&page=1'
    payload = "{}"
    response = requests.request("GET", url, data=payload,verify=False)
    result=response.json()
    l=[]
    for i in result['results']:
        title=exit_or_not('title', i)
        vote_average=exit_or_not('vote_average', i)
        original_language=exit_or_not('original_language', i)
        overview=exit_or_not('overview', i)
        release_date=exit_or_not('release_date', i)
        movie_id=exit_or_not('id', i)
        if i['poster_path']==None:
            poster="tmdb/images/n.jpg"
        else:
            poster='https://image.tmdb.org/t/p/w185'+i['poster_path']
        path=get_trailer(title)
        if path!=None:
            path='https://www.youtube.com/watch?v='+path 
        a = Playing(title=title,image=poster,original_language=original_language,overview=overview,release_date=release_date,movie_id=movie_id,vote_average=vote_average,trailer=path)
        a.save()
 
        l.append(a)
    return render(request, 'tmdb/popular.html', {'l': l})
        
        
        
def test(request):
   
        url='https://api.themoviedb.org/3/movie/upcoming?api_key=1c7b5989619b35104b3713869fdd3ca9&language=en-US&page=1'
        payload = "{}"
        response = requests.request("GET", url, data=payload,verify=False)
        result=response.json()
        d=dict()
        b=datetime.datetime.now()
      
        diff=datetime.timedelta(days=1)
        for i in result['results']:
            a=datetime.datetime.strptime(i['release_date'],'%Y-%m-%d')
            if (a-b)>diff:
                if i['backdrop_path']==None:
                    poster="tmdb/images/n.jpg"
                else:
                    poster='https://image.tmdb.org/t/p/w780'+i['backdrop_path']
              
                d[i['release_date']]=d.get(i['release_date'],(poster,i['id']))
       
        l=d.keys()
        l.sort()
        k=[]
        for i in l :
            
            a = Image(image=d[i][0],movie_id=d[i][1])
            a.save()
            k.append(a)
        return render(request, 'tmdb/test.html', {'k': k})
    
        
        

            
    

        









#     return HttpResponse("Hello, world. You're at the polls index.")