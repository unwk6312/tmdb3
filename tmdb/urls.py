from django.conf.urls import url

from . import views

app_name = 'tmdb'
urlpatterns = [

    url(r'^(?P<name>[a-zA-Z]+)$', views.search, name='search'),
    url(r'^(?P<id>[0-9]+)/details/$', views.details, name='details'),
    

    
]