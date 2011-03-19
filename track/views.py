# Create your views here.
from django.core import serializers
from track.models import Track, Playlist, Preset, TrackPass
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
    
    playlist_json = tracks_to_json_playlist(tracks, playlist)
    
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
    preset = Preset.objects.filter(id=preset_id)
    preset_json = serializers.serialize("json", preset)
    
    return HttpResponse(preset_json, content_type='application/json')


def tracks_to_json_playlist(tracks, playlist=None):
    '''
    Takes a queryset of tracks and returns a json playlist
    '''
    #Restrict tracks to published tracks
    #tracks = tracks.filter(published=True)
    
    playlist_tracks = []
    
    for track in tracks:
        track_dict = track.__dict__
        track_dict["artist"] = str(track.artist)
        del track_dict["_state"]
        del track_dict["_artist_cache"]
        playlist_tracks.append(track_dict)
    
    if playlist:
        playlist_dict = {
            "id":     playlist.id,
            "name":   playlist.name,
            "tracks": playlist_tracks
        }
    else:
        playlist_dict = {
            "id":     -1,
            "name":   "new",
            "tracks": playlist_tracks
        }
    
    playlist_json = json.dumps(playlist_dict)
    return playlist_json

def playlist_generate(request):
    '''
    Provides the GET verb for /playlist/generate/ with
     - posativity
     - aggression
     - speed
     - suspense
    arguements
    '''
    p = request.get("positivity", 1)
    a = request.get("aggression", 1)
    sp = request.get("speed", 1)
    su = request.get("suspense", 1)
    
    genreDict = {}
    playlist = TrackPass.objects.all()
    
    #Add all tracks to a dictionary with the track as the key deviation as value
    count = float(0) #FLOAT'd'd!!!
    for track in playlist:
        count = count + 1
        deviation = int(getDeviation(p,a,sp,su,track))
        try:
            genreDict[deviation]
            genreDict[deviation + count/100] = track
        except KeyError:
            genreDict[deviation] = track
    sorted_track_passes = sortTracks(genreDict)
    
    tracks = []
    for trackpass in sorted_track_passes:
        try:
            tracks.append(Track.objects.get(pk=trackpass.track.id,published=True))
        except:
            pass #drop non-published tracks
    
    playlist_json = tracks_to_json_playlist(tracks)
    return HttpResponse(playlist_json, content_type='application/json')

def getDeviation(positivity,aggression,speed,suspense,track):
    """
    Compare the searched-for parameters with a track,
    return the deviation from the track
    TODO: use the sum of the squares
    """
    deviationSpeed = int(positivity) - int(track.positivity)
    deviationCombat = int(aggression) - int(track.aggression)
    deviationSuspense = int(speed) - int(track.speed)
    deviationPositive = int(suspense) - int(track.suspense)

    deviation = abs(deviationSpeed) \
        + abs(deviationCombat) \
        + abs(deviationSuspense) \
        + abs(deviationPositive)

    return deviation

def sortTracks(genreDict):
    """
    Takes a dictionary of deviation:track, sorts it by deviation,
    and returns the ordered list of tracks
    """
    return [genreDict[key] for key in sorted(genreDict.keys())]
