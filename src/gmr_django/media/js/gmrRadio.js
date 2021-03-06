/*
 * gmrRadio
 * Loads and manipulates a playlist of tracks
 * namespace: gmr.radio
 * dependencies: jquery 1.4.4, gmrPlayer
 */
  
gmr.radio = function() {
  //private


  return {
    //public
    playlist : '',
    player : gmr.player,
    currentTrack : 0,
    mediaURL : 'http://' + document.domain + ':' + document.location.port + '/site_media/',

    loadPlaylist : function(playlistID) {
      $.ajax({
        url: "/playlist/1",
        context: document.body,
        contentType: 'application/json',
        success: function(response){
          gmr.radio.playlist = response;
          console.log(gmr.radio.playlist);
          gmr.radio.currentTrack = 0;
          $(gmr.radio.player.audio).empty();
          gmr.radio.player.addSource(gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].ogg);
          gmr.radio.player.addSource(gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].mp3);
          console.log('Adding: ' + gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].ogg);
          gmr.radio.player.play();
        }
      });
    },

    generatePlaylist : function(positivity, aggression, speed, suspense) {
      $.ajax({
        url: "/playlist/generate",
        context: document.body,
        data: 
          'positivity=' + positivity + '&' +
          'aggression=' + aggression + '&' +
          'speed=' + speed + '&' +
          'suspense=' + suspense,          
        contentType: 'application/json',
        success: function(response){
          gmr.radio.playlist = response;
          console.log(gmr.radio.playlist);
          gmr.radio.currentTrack = 0;
          $(gmr.radio.player.audio).empty();
          gmr.radio.player.addSource(gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].ogg);
          gmr.radio.player.addSource(gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].mp3);
          console.log('Adding: ' + gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].ogg);
          gmr.radio.player.play();
          gmr.radio.updatePlaylist();
        }
      });
    },
    
    savePlaylist : function() {
      $.ajax({
        type: 'POST',
        url: '',
        data: gmr.radio.playlist,
        success: function() {}
      })
    },

    next : function() {
      if (gmr.radio.currentTrack < (gmr.radio.playlist.tracks.length - 1)) {
        console.log(gmr.radio.currentTrack);
        gmr.radio.currentTrack++;
        gmr.radio.player.stop();
        $(gmr.radio.player.audio).empty();
        console.log(gmr.radio.currentTrack + ' : ' + gmr.radio.playlist.tracks[gmr.radio.currentTrack]);
        gmr.radio.player.addSource(gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].ogg);
        gmr.radio.player.addSource(gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].mp3);
        gmr.radio.player.play();
        gmr.radio.updatePlaylist();
      } else {
        //end of playlist
        console.log('No more tracks');
        gmr.radio.jumpTo(0);
        gmr.radio.player.play();
      }
    },

    previous : function() {
      if (gmr.radio.currentTrack > 0) {
        console.log(gmr.radio.currentTrack);
        gmr.radio.currentTrack--;
        gmr.radio.player.stop();
        $(gmr.radio.player.audio).empty();
        console.log(gmr.radio.currentTrack + ' : ' + gmr.radio.playlist.tracks[gmr.radio.currentTrack]);
        gmr.radio.player.addSource(gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].ogg);
        gmr.radio.player.addSource(gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].mp3);
        gmr.radio.player.play();
        gmr.radio.updatePlaylist();
      } else {
        //end of playlist
        console.log('At first track');
      }
    },

    assignPlayerCallback : function() {
      gmr.radio.player.assignEndCallback(gmr.radio.next);
    },

    updatePlaylist : function() {
      $('#playlist').empty();
      for (var i in gmr.radio.playlist.tracks) {
        var liExtra = '';
        if (gmr.radio.currentTrack == i) { liExtra = ' class="playing"' }
        $('#playlist').append('<li' + liExtra + '><a onclick="gmr.radio.jumpTo(' + i + ');">' + gmr.radio.playlist.tracks[i].name + '</a></li>');
      }
    },

    jumpTo : function(track) {
      if (track < (gmr.radio.playlist.tracks.length)){
        gmr.radio.currentTrack = track;
        gmr.radio.updatePlaylist();
        gmr.radio.player.stop();
        $(gmr.radio.player.audio).empty();
gmr.radio.player.addSource(gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].ogg);
        gmr.radio.player.addSource(gmr.radio.mediaURL + gmr.radio.playlist.tracks[gmr.radio.currentTrack].mp3);
        gmr.radio.player.play();
      } 
    }
  }
}();

gmr.radio.assignPlayerCallback();

console.log(gmr.radio.player.audio)
