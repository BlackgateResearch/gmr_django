from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<track_id>\d+)/$', 'track.views.track_get'),
)
