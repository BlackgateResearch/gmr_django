from django.conf.urls.defaults import *
from track.views import track

urlpatterns = patterns('',
    (r'^(?P<track_id>\d+)/$', 'track.views.track_get'),
)