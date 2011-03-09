from django.db import models

class Track(models.Model):
    '''
    Stores track information
    '''
    artist =      models.ForeignKey('artist.Artist')
    name =        models.CharField(max_length = 50)
    description = models.TextField()
    mp3 =         models.FileField(upload_to="track/")
    ogg =         models.FileField(upload_to="track/")
    published =   models.BooleanField()
    
    def __unicode__(self):
        return unicode(self.artist) + u' - ' + self.name


class Track_vote(models.Model):
    '''
    Ensures a user can only vote on a track once.
    TODO: wipe this once a week? Maybe use a bool
    '''
    track =     models.ForeignKey('track.Track')
    user =      models.ForeignKey('auth.User')
    vote_time = models.TimeField()
    

class Track_pass(models.Model):
    '''
    TODO: Does oli-charlesworth's solution work?
    http://stackoverflow.com/questions/4642524/maths-approximating-the-mean-without-storing-the-whole-data-set
    How about storing the cumulative vote count, and the number of votes?
    (i.e. total=total+vote, numVotes=numVotes+1).
    That way, you can get the exact mean by dividing one by the other.
    '''
    track =      models.ForeignKey('track.Track')
    positivity = models.IntegerField()
    aggression = models.IntegerField()
    speed =      models.IntegerField()
    suspense =   models.IntegerField()
    votes =      models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Track Passes"


class Preset(models.Model):
    '''
    A user's PASS preset, named.
    '''
    name =       models.CharField(max_length = 50)
    positivity = models.IntegerField()
    aggression = models.IntegerField()
    speed =      models.IntegerField()
    suspense =   models.IntegerField()
    user =       models.ForeignKey('auth.User')

    def __unicode__(self):
        return unicode(self.name)

class Playlist(models.Model):
    '''
    A named track container, linking table, PlaylistTrack.
    '''
    name =   models.CharField(max_length = 50)
    user =   models.ForeignKey('auth.User')
    tracks = models.ManyToManyField('Track', through='PlaylistTrack')
    
    def __unicode__(self):
        return self.name
        
        
class PlaylistTrack(models.Model):
    '''
    A linking table between Playlist and Track, identifying if a Track
    is in a Playlist
    '''
    playlist = models.ForeignKey('track.Playlist')
    track =    models.ForeignKey('track.Track')
    position = models.IntegerField()

    def __unicode__(self):
        return unicode(self.playlist) + ': ' + unicode(self.track)
        
    class Meta:
        ordering = ['position']
    
    
class Play(models.Model):
    '''
    A log of when a user played a track, and how long they listened
    to it for.
    '''
    user =        models.ForeignKey('auth.User')
    track =       models.ForeignKey('track.Track')
    played_time = models.DateTimeField()
    duration =    models.IntegerField()
    

'''
#integrated into Play
class PlayToEnd(models.Model):
    user =          models.ForeignKey('auth.User')
    track =         models.ForeignKey('track.Track')
    finished_time = models.DateTimeField()
'''
