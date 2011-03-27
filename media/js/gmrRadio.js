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
        url: "/playlist/list",
        context: document.body,
        success: function(response){
          gmr.radio.playlist = response;
          console.log(gmr.radio.playlist);
        }
      });
      gmr.radio.currentTrack = 0;
    },
    
    savePlaylist : function() {
      
    },

    next : function() {
      if (true) {
        console.log(gmr.radio.playlist.length);
        gmr.radio.currentTrack++;
      } else {

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
