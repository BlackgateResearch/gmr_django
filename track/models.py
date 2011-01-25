from django.db import models
import settings

class Track(models.Model):
    artist =      models.ForeignKey('artist.Artist')
    name =        models.CharField(max_length = 50)
    description = models.TextField()
    mp3 =         models.FileField(upload_to="track/")
    ogg =         models.FileField(upload_to="track/")
    
    def __unicode__(self):
        return unicode(self.artist) + u' - ' + self.name


class Track_vote(models.Model):
    track =     models.ForeignKey('track.Track')
    user =      models.ForeignKey('auth.User')
    vote_time = models.TimeField()
    

class Track_pass(models.Model):
    track =      models.ForeignKey('track.Track')
    positivity = models.IntegerField()
    aggression = models.IntegerField()
    speed =      models.IntegerField()
    suspense =   models.IntegerField()
    votes =      models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Track Passes"


class Preset(models.Model):
    name =       models.CharField(max_length = 50)
    positivity = models.IntegerField()
    aggression = models.IntegerField()
    speed =      models.IntegerField()
    suspense =   models.IntegerField()
    user =       models.ForeignKey('auth.User')


class Playlist(models.Model):
    name = models.CharField(max_length = 50)
    user = models.ForeignKey('auth.User')



class PlaylistTrack(models.Model):
    playlist = models.ForeignKey('track.Playlist')
    track =    models.ForeignKey('track.Track')
    position = models.IntegerField()
  
    
class Play(models.Model):
    user =        models.ForeignKey('auth.User')
    track =       models.ForeignKey('track.Track')
    played_time = models.DateTimeField()
    
    
class PlayToEnd(models.Model):
    user =          models.ForeignKey('auth.User')
    track =         models.ForeignKey('track.Track')
    finished_time = models.DateTimeField()
