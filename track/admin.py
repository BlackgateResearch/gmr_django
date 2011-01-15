from track.models import Track, Preset, Track_pass, Track_vote
from track.models import Playlist, PlaylistTrack 
from track.models import Play, PlayToEnd
from django.contrib import admin

admin.site.register(Track)
admin.site.register(Preset)
admin.site.register(Playlist)
admin.site.register(PlaylistTrack)
admin.site.register(Play)
admin.site.register(PlayToEnd)
admin.site.register(Track_pass)
admin.site.register(Track_vote)