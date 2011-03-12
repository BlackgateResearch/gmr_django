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

    loadPlaylist : function() {
      $.ajax({
        url: "/playlist/list",
        context: document.body,
        success: function(response){
          gmr.radio.playlist = response;
          console.log(gmr.radio.playlist);
        }
      });
    },
    
    savePlaylist : function() {
      
    },

    next : function() {
      
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
