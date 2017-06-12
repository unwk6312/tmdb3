from django.conf.urls import url

from . import views

app_name = 'tmdb'
urlpatterns = [
   
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>[\w+\s]+)/$', views.search, name='search'),

    url(r'^(?P<id>[0-9]+)/details/$', views.details, name='details'),
    url(r'^people/(?P<name>[a-zA-Z\s]+)/$', views.search1, name='search1'),
    url(r'^bio/(?P<id>[0-9]+)/$', views.search2, name='search2'),
    url(r'^news/today/$', views.playing, name='playing'),
    url(r'^news/coming/$', views.upcoming, name='upcoming'),
    url(r'^news/popular/$', views.popular, name='popular'),
     url(r'^news/popular/test$', views.test, name='test'),
    
]
    

    