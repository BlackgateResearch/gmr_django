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
    tracks : '',
    player : gmr.player,

    loadPlaylist : function() {
      
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
gmr.radio.player.addSource('http://127.0.0.1:8000/site_media/track/itcrowd.ogg');
gmr.radio.player.addSource('http://127.0.0.1:8000/site_media/track/itcrowd.mp3');
gmr.radio.player.outputTag();
console.log(gmr)

