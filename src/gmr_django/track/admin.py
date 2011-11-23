from track.models import Track, Preset, TrackVote
from track.models import Playlist, PlaylistTrack 
from track.models import Play
from django.contrib import admin

class TrackAdmin(admin.ModelAdmin):
    list_display = ('artist', 'name', 'description')
    list_filter = ('published',)
    search_fields = ['artist__name', 'name', 'description']
    
admin.site.register(Track, TrackAdmin)


admin.site.register(Preset)
admin.site.register(Playlist)
admin.site.register(PlaylistTrack)
admin.site.register(Play)
admin.site.register(TrackVote)
