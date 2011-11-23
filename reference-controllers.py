# coding: utf8

if False:
    from gluon.globals import *
    from gluon.html import *
    from gluon.http import *
    from gluon.sqlhtml import SQLFORM, SQLTABLE, form_factory
    session = Session()
    request = Request()
    response = Response()

import operator, datetime

#########################################################################
## This is the radio controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################  

@auth.requires_login()
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


@auth.requires_login()
def getArtists():
    """
    Return all artists as a Dictionary
    >>> isinstance(len(db().select(db.artist.ALL)),int)
    True
    """
    return artistsDict(db().select(db.artist.ALL))

def loginAsTestUser():
    """
    Aid to testing, allows code to be run as though user is logged in.
    Does not function if called from web.
    """
    from gluon.storage import Storage     
    session.auth=Storage() 
    session.auth.user_id = 1

@auth.requires_login()
def artistsDict(artists):
    """
    Creates a dictionary containing the artist [id -> name]
    Input is a list of artist db objects

    >>> loginAsTestUser()
    >>> isinstance(len(artistsDict(db().select(db.artist.ALL))),int)
    True
    """
    artistDict = {}
    for artist in artists:
        artistDict[artist.id] = artist.name
    return artistDict


@auth.requires_login()
def index():
    """
    Home page for GMR
    """
    return dict(
        playlists = getPlaylists()['playlists'],
        presets = getPresets()['presets']
        
    )


@auth.requires_login()
def jsArtistLookup():
    """
    Ajax method for converting artist ID (int) to artist name (String)
    """
    return artistLookup(int(request.args(0)))


@auth.requires_login()
def artistLookup(id):
    """
    Method for converting artist ID (int) to artist name (String)
    Seems like it could be integrated into jsArtistLookup, but both provide
    distinct functionality that makes the view readable.
    """
    return getArtists()[id]


@auth.requires_login()
def getTrack():
    """
    Gets a track object, given it's ID
    """
    trackID = request.args(0)
    today = datetime.date.today()    
    
    hasBeenNudged = bool(
        db(
            (db.nudge.nudgeTime==today) &
            (db.nudge.user_id==auth.user.id) &
            (db.nudge.track_id==trackID)
        ).select()
    )
    
    return dict(
        track = db(db.track.id == trackID).select()[0],
        hasBeenNudged = hasBeenNudged
    )


@auth.requires_login()
def nextTrack():
    """
    Returns the next track object, while simultaniously popping it off the end
    of the playlist
    """
    if (len(session.currentPlaylist) > 0):
        return dict(
            track = session.currentPlaylist.pop(0),
            end = False
        )
    else:
        return dict(end=True)


@auth.requires_login()
def getPlaylist():
    """
    Returns the current playlist (List of Track objects)
    """
    return dict(
        currentPlaylist = session.currentPlaylist,
        lookupArtist = getArtists()
    )


@auth.requires_login()
def queuePASS():
    """
    Returns playlist, given PASS query
    """
    return dict(
        playlist = createPASSPlaylist(),
        lookupArtist = getArtists()
    )

@auth.requires_login()
def queuePlaylist():
    """
    Returns playlist, given playlist ID query
    """
    return dict(
        playlist = createPlaylist(), #TODO: This is hax
        lookupArtist = getArtists()
    )

@auth.requires_login()
def previewPlaylist():
    """
    Returns a playlist to user, given PASS query, with arists dictionary for
    looking up
    """
    return dict(
    playlist = createPlaylist(),
    lookupArtist = getArtists()
    )


@auth.requires_login()
def createPASSPlaylist():
    """
    Returns playlist, given PASS query
    TODO: Make this work more than accidentally!
    """
    #args
    p = request.args(0) #positivity
    a = request.args(1) #aggression
    sp = request.args(2) #speed
    su = request.args(3) #suspense
    
    genreDict = {}
    playlist = db().select(db.track.ALL)

    #Add all tracks to a dictionary with the track as the key deviation as value
    count = 0.1 #FLOAT'd'd!!!
    for track in playlist:
        count = count + 1
        deviation = int(getDeviation(p,a,sp,su,track))
        
        try:
            genreDict[deviation]
            genreDict[deviation + count/100] = track
        except KeyError:
            genreDict[deviation] = track
    return sortTracks(genreDict)


@auth.requires_login()
def createPlaylist():
    """
    Returns playlist, given playlistID
    """
    #args
    playlistID = int(request.args(0))
    
    query = (db.track.id == db.playlist_track.track_id) & \
        (db.playlist_track.playlist_id == playlistID)
    
    tracks = db(query).select(db.track.ALL,orderby=db.playlist_track.position)
   
    return tracks

@auth.requires_login()
def sortTracks(genreDict):
    """
    Takes a dictionary of deviation:track, sorts it by deviation,
    and returns the ordered list of tracks
    """
    return [genreDict[key] for key in sorted(genreDict.keys())]


@auth.requires_login()
def createPreset():
    """
    Creates a preset for the currently logged-in user
    """
    name = request.vars.name
    positivity = request.vars.positivity
    aggression = request.vars.aggression
    speed = request.vars.speed
    suspense = request.vars.suspense
    
    preset = db.preset.insert(
        name=name,
        positivity = positivity,
        aggression = aggression,
        speed = speed,
        suspense = suspense,
        user_id = auth.user.id
    )
    return(dict(preset = preset))
    
    
@auth.requires_login()
def getPresets():
    """
    Returns an alphabetical list of the currently logged-in user's presets
    """
    return(
        dict(presets = db(
            db.preset.user_id==auth.user.id
            ).select(
                db.preset.ALL,orderby=db.preset.name
            )
        )
    )

@auth.requires_login()
def getPlaylists():
    """
    Returns an alphabetical list of the currently logged-in user's playlists
    """
    playlists = db(db.playlist.user_id==auth.user.id).select(
            db.playlist.ALL,orderby=db.playlist.name)
    return(
        dict(playlists = playlists)
    )

@auth.requires_login()
def updatePlaylist():
    """
    Creates new playlist, or updates existing
    TODO: a little long, consider refactoring
    """
    playlistID = int(request.args(0))
    playlistName = request.args(1) 
    
    trackCount = 0
    for item in request['args']:
        trackCount = trackCount + 1
    trackCount = trackCount - 2
    
    if playlistID==0:
        playlist = db.playlist.insert(
            name = playlistName,
            user_id = auth.user.id
        )
        playlistID = playlist.id
    else:
        playlistID = playlistID

    if not playlistBelongsToUser(playlistID):
        raise HTTP(401)
    else:
        db(db.playlist_track.playlist_id==playlistID).delete()
    
    dictionary = {}
    for position in range(trackCount):
        pos = position + 2
        dictionary[position]=request.args(pos)

    for position in range(trackCount-1):
        playListTrack = db.playlist_track.insert(
            playlist_id = playlistID,
            track_id = dictionary[position],
            position = position
        )
    return(dictionary)   

def playlistBelongsToUser(playlistID):
    """
    Checks wether a playlist (given by id) belongs to the current user
    """  
    authorised = False
    thePlaylist = db(db.playlist.id==playlistID).select()[0]
    
    #Can I see your papers?
    if (thePlaylist.user_id == auth.user.id): 
        #Move along
        authorised = True 
    else:
        #Your german is very good
        #Thank you
        authorised = False
    return authorised

def presetBelongsToUser(presetID):
    """
    Checks wether a preset (given by id) belongs to the current user
    TODO: Discuss wheather this redundancy is worth it, re playlistBelongsToUser
    """  
    authorised = False
    thePreset = db(db.preset.id==presetID).select()[0]
    
    #Can I see your papers?
    if (thePreset.user_id == auth.user.id): 
        #Move along
        authorised = True 
    else:
        #Your german is very good
        #Thank you
        authorised = False 
    return authorised

@auth.requires_login()
def getPlaylistTracks():
    """
    Returns a list of tracks for a given playlist ID
    """  
    playlistID = int(request.args(0))  
        
    if not playlistBelongsToUser(playlistID):
        raise HTTP(401)
    else:
        pass
    query = (db.track.id == db.playlist_track.track_id) & \
        (db.playlist_track.playlist_id == playlistID)
    
    tracks = db(query).select(db.track.ALL,orderby=db.playlist_track.position)
    
    return(
        dict(
        tracks = tracks,
        lookupArtist = getArtists()
        )
    )


@auth.requires_login()
def deletePreset():
    """
    Delete a preset
    """
    presetID = request.args(0)
    
    if not presetBelongsToUser(presetID):
        raise HTTP(401)
    else:
        pass   
    db(db.preset.id==presetID).delete()
    
    return("OK")


@auth.requires_login()
def deletePlaylist(): 
    """
    Delete a playlist
    """
    playlistID = request.args(0)
    
    if not playlistBelongsToUser(playlistID):
        raise HTTP(401)
    else:
        pass
            
    db(db.playlist_track.playlist_id==playlistID).delete()
    
    db(db.playlist.id==playlistID).delete()


@auth.requires_login()
def trackPlayed():
    """
    Logs when a track starts to play, and which user played it
    """
    checkin = db.played.insert(
        track_id=request.vars.track,
        playedTime=datetime.datetime.now(),
        user_id = auth.user.id
    )
    return dict(checkin = checkin)


@auth.requires_login()
def trackPlayedToEnd():
    """
    Logs when a track has played all the way through,
    and which user played it
    """
    checkin = db.played_to_end.insert(
        track_id=request.vars.track,
        playedTime=datetime.datetime.now(),
        user_id = auth.user.id
    )
    return dict(checkin = checkin)


@auth.requires_login()
def nudge():
    """
    Nudges the track up or down a single pass variable.
    Not more than once per 24h
    nudge/trackID/0-3(pass)/u-or-d
    """
    trackID = request.args(0)
    passVar = int(request.args(1))
    direction = str(request.args(2))

    if direction == "u":
        nudgeValue = 1
    else:
        nudgeValue = -1
    
    today = datetime.date.today()

    hasBeenNudged = db(
        (db.nudge.nudgeTime==today) &
        (db.nudge.user_id==auth.user.id) &
        (db.nudge.track_id==trackID)
    ).select()
    
    if not bool(hasBeenNudged):
        
        track = db(db.track.id==trackID).select()[0]

        if passVar == 0:
            track.update_record(positivity = track.positivity + nudgeValue)
        if passVar == 1:
            track.update_record(aggression = track.aggression + nudgeValue)
        if passVar == 2:
            track.update_record(speed = track.speed + nudgeValue)
        if passVar == 3:
            track.update_record(suspense = track.suspense + nudgeValue)
        else:
            pass

        nudge = db.nudge.insert(
            track_id=trackID,
            nudgeTime=datetime.date.today(),
            user_id = auth.user.id,
            pass_attribute = passVar,
            direction = direction
        )
        
        return dict(
            track = track,
            nudge = nudge,
            hasBeenNudged = hasBeenNudged
        )

    raise HTTP(401)
    

def user():
    """
    exposes:
    http://..../[app]/default/user/login 
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@auth.requires_login()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)
