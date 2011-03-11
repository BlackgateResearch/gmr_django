# Create your views here.
from django.core import serializers
from track.models import Track, Playlist, Preset
from django.http import HttpResponse
import settings 
from collections import namedtuple
import json
from django.shortcuts import get_object_or_404

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
    
    #track = Track.objects.filter(id=track_id)
    #track_json = serializers.serialize("json", track)
    #return HttpResponse(track_json, content_type='application/json')
    
    #unimplemented for now
    response = HttpResponse()
    response.status_code=501
    return response

def playlist_get(request, playlist_id):
    '''
    Provides the GET verb for /playlist/id
    Returns a json playlist object in format:
    
    {
        "tracks": [
            {
                "description": "I love that show.",
                "artist": "Namtao",
                "ogg": "track/itcrowd.ogg",
                "mp3": "track/itcrowd.mp3",
                "artist_id": 1,
                "id": 1,
                "name": "IT Crowd Theme" 
            } 
        ],
        "id": 1,
        "name": "first_playlist"
    }
    '''
    playlist = get_object_or_404(Playlist,pk=playlist_id)
    tracks = Playlist.objects.get(pk=playlist_id).tracks.all()
    
    playlist_tracks = []
    
    for track in tracks:
        track_dict = track.__dict__
        track_dict["artist"] = str(track.artist)
        del track_dict["_state"]
        del track_dict["_artist_cache"]
        playlist_tracks.append(track_dict)
    
    playlist_dict = {
        "id":     playlist.id,
        "name":   playlist.name,
        "tracks": playlist_tracks
    }
    
    playlist_json = json.dumps(playlist_dict)
    
    return HttpResponse(playlist_json, content_type='application/json')
    

def playlist_list(request):
    playlists = serializers.serialize("json", Playlist.objects.filter(user=request.user))
    
    return HttpResponse(playlists, content_type='application/json')


def preset_list(request):
    playlists = serializers.serialize("json", Preset.objects.filter(user=request.user))
    
    return HttpResponse(playlists, content_type='application/json')


def preset_get(request, preset_id):
    '''
    Provides the GET verb for /preset/id
    Returns a json playlist object in format:
    
    {
        "tracks": [
            {
                "description": "I love that show.",
                "artist": "Namtao",
                "ogg": "track/itcrowd.ogg",
                "mp3": "track/itcrowd.mp3",
                "artist_id": 1,
                "id": 1,
                "name": "IT Crowd Theme" 
            } 
        ],
        "id": 1,
        "name": "first_playlist"
    }
    '''
    preset = get_object_or_404(Preset,pk=preset_id)

    
    preset_json = json.dumps(preset)
    
    return HttpResponse(preset_json, content_type='application/json')
