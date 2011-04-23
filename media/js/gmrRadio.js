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

    loadPlaylist : function() {
      $.ajax({
        url: "/playlist/1",
        context: document.body,
        success: function(response){
          gmr.radio.playlist = response;
          console.log(gmr.radio.playlist);
          gmr.radio.currentTrack = 0;
          $(gmr.radio.player.audio).empty();
          gmr.radio.player.addSource('http://127.0.0.1:8000/site_media/' + gmr.radio.playlist.tracks[gmr.radio.currentTrack].ogg);
          gmr.radio.player.addSource('http://127.0.0.1:8000/site_media/' + gmr.radio.playlist.tracks[gmr.radio.currentTrack].mp3);
          console.log('Adding: ' + 'http://127.0.0.1:8000/site_media/' + gmr.radio.playlist.tracks[gmr.radio.currentTrack].ogg);
          gmr.radio.player.play();
        }
      });
    },
    
    savePlaylist : function() {
      
    },

    next : function() {
      if (gmr.radio.currentTrack < (gmr.radio.playlist.tracks.length - 1)) {
        console.log(gmr.radio.currentTrack);
        gmr.radio.currentTrack++;
        $(gmr.radio.player.audio).empty();
        console.log(gmr.radio.currentTrack + ' : ' + gmr.radio.playlist.tracks[gmr.radio.currentTrack]);
        gmr.radio.player.addSource('http://127.0.0.1:8000/site_media/' +gmr.radio.playlist.tracks[gmr.radio.currentTrack].ogg);
        gmr.radio.player.addSource('http://127.0.0.1:8000/site_media/' +gmr.radio.playlist.tracks[gmr.radio.currentTrack].mp3);
        gmr.radio.player.play();
      } else {
        //end of playlist
        console.log('No more tracks');
      }
    },

    previous : function() {
      
    },

    pause : function() {
      
    },

    assignPlayerCallback : function() {
      gmr.radio.player.assignEndCallback(gmr.radio.next);
    }
  }
}();

gmr.radio.assignPlayerCallback();

console.log(gmr.radio.player.audio)
