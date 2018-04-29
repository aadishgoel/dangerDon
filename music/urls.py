from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

app_name = 'music'

urlpatterns=[

    #/music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/music/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),    

    #/music/login/
    url(r'^login/$', login, {'template_name':'music/login.html'}, name='login'),

    #/music/logout/
    url(r'^logout/$', logout, name='logout'),

    #music/album/add/
    url(r'^album/add/$' , views.AlbumCreate.as_view(), name='album-add'),

    #/music/<pk>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #music/album/<pk>/
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #music/album/<pk>/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # music/album/<pk>/like/
    url(r'^album/(?P<pk>[0-9]+)/like/$', views.Like.as_view(), name='album-like'),

    # music/album/<pk>/dislike/
    url(r'^album/(?P<pk>[0-9]+)/dislike/$', views.Dislike.as_view(), name='album-dislike'),

    ]
