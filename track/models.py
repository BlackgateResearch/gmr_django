from django.db import models

class Track(models.Model):
    artist = models.ForeignKey('artist.Artist')
    name = models.CharField(max_length = 50)
    description = models.TextField()
    mp3 = models.FileField(upload_to="track/")
#   PASS
    positivity = models.IntegerField()
    aggression = models.IntegerField()
    speed = models.IntegerField()
    suspense = models.IntegerField()


class Preset(models.Model):
    name = models.CharField(max_length = 50)
    positivity = models.IntegerField()
    aggression = models.IntegerField()
    speed = models.IntegerField()
    suspense = models.IntegerField()
    user = models.ForeignKey('auth.User')


class Playlist(models.Model):
    name = models.CharField(max_length = 50)
    user = models.ForeignKey('auth.User')


class PlaylistTrack(models.Model):
    playlist = models.ForeignKey('track.Playlist')
    track = models.ForeignKey('track.Track')
    position = models.IntegerField()


# We'll phase out nudges in favor of a average-based pass
class Nudge(models.Model):
    user = models.ForeignKey('auth.User')
    track = models.ForeignKey('track.Track')
    nudge_time = models.TimeField()
    pass_attribute = models.IntegerField()
    nudged_up = models.BooleanField()
    
    
class Play(models.Model):
    user = models.ForeignKey('auth.User')
    track = models.ForeignKey('track.Track')
    played_time = models.DateTimeField()
    
class PlayToEnd(models.Model):
    user = models.ForeignKey('auth.User')
    track = models.ForeignKey('track.Track')
    finished_time = models.DateTimeField()
