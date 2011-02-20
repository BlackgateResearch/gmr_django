# Create your views here.
from django.core import serializers
from track.models import Track, PlaylistTrack
from django.http import HttpResponse
import settings 

def track_get(request, track_id):
    '''
    Provides the GET verb for /track/id
    Returns a json array with the single specified track in format:
    
    [{
        "pk": 1,
        "model": "track.track",
        "fields": {
            "description": "test",
            "mp3": "track/song.mp3",
            "name": "test",
            "artist": 1
        }
    }]
    '''
    
    track = Track.objects.filter(id=track_id)
    track_json = serializers.serialize("json", track)
    return HttpResponse(track_json, content_type='application/json')

def playlist_get(request, playlist_id):
    '''
    Provides the GET verb for /playlist/id
    Returns a json array of tracks in format:
    
    [
        {
            "pk": 1,
            "model": "track.track",
            "fields": {
                "description": "I love that show.",
                "ogg": "track/itcrowd.ogg",
                "mp3": "track/itcrowd.mp3",
                "name": "IT Crowd Theme",
                "artist": 1
            }
        },
        {
            "pk": 1,
            "model": "track.track",
            "fields": {
                "description": "I love that show.",
                "ogg": "track/itcrowd.ogg",
                "mp3": "track/itcrowd.mp3",
                "name": "IT Crowd Theme",
                "artist": 1
            }
        }
    ]
    '''
    
    playlist = Track.objects.filter(playlisttrack__playlist__exact=playlist_id)
    playlist_json = serializers.serialize("json", playlist)
    return HttpResponse(playlist_json, content_type='application/json')
