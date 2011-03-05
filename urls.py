from django.conf.urls.defaults import *
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin_tools/', include('admin_tools.urls')),
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),

    (r'^radio/', include('radio.urls')),
    (r'^track/', include('track.urls')),
    (r'^playlist/(?P<playlist_id>\d+)/$', 'track.views.playlist_get'),
    (r'^playlist/list/', 'track.views.playlist_list'),
)

'''
URL                 Verb         Return value
/track/id           GET          track.json

/playlist/list      GET          array of playlists
/playlist/id        GET          playlist.json
/playlist/          POST         playlist.json
/playlist/id        DELETE       200 OK
/playlist/id        UPDATE       playlist.json

[presets: as playlists]

/playlist/current/  GET         playlist.json
/playlist/current/  POST        playlist.json
'''
