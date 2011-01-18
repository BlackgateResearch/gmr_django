# Create your views here.
from django.core import serializers
from track.models import Track
from django.http import HttpResponse
import settings 

def track(request, track_id):
    '''
    Provides the GET verb for /track/id
    Returns a json document of the specified track in format:
    
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
    track[0].url = settings.MEDIA_URL + u'track/' + str(track[0].pk)
    track_json = serializers.serialize("json", track)
    return HttpResponse(track_json, content_type='application/json')