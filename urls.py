from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    # Example:
    # (r'^gmr_django/', include('gmr_django.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),

    (r'^radio/', include('radio.urls')),
    (r'^track/', include('track.urls')),
    
    (r'^playlist/(?P<playlist_id>\d+)/$', 'track.views.playlist_get'),
)

'''
URL                 Verb         Return value
/track/id           GET          track.json

/playlist/list      GET          array of playlists
/playlist/id        GET          playlist.json
/playlist/          PUSH         playlist.json
/playlist/id        DELETE       200 OK
/playlist/id        UPDATE       playlist.json

[presets: as playlists]

/playlist/current/  GET         playlist.json
/playlist/current/  PUSH        playlist.json
'''