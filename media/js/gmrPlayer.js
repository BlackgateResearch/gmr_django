/*
 * gmrPlayer
 * Privides an HTML5 audio player
 * namespace: gmr.player
 * dependencies: jquery 1.4.4
 */

gmr.player = function() {
  //private
   

  return {
    //public
    
    //The <audio> tag
    audio : $('<audio>', {  
      autoPlay : 'autoplay',  
      controls : 'controls'  
    }),
    
    //Reference to a callback function
    endCallback : null,
    
    //Add a <source> tag to <audio> tag with the src 'path'
    addSource : function(path) {
      $('<source>').attr('src', path).appendTo(gmr.radio.player.audio);
    },
    
    //Sets the callback for the onended event
    assignEndCallback : function(callback) {
      gmr.player.endCallback = callback;
      $(gmr.player.audio).bind('ended', gmr.player.endCallback);
    },
    
    play : function() {
      gmr.player.audio[0].play();
    },
    
    pause : function() {
      gmr.player.audio[0].pause(); 
    },
   
    stop : function() {
      gmr.player.audio[0].pause();
      gmr.player.audio[0].currentTime = 0;
    }       
  }
}();
