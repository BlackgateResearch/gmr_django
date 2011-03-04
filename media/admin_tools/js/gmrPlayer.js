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
      $('<source>').attr('src', path).appendTo(gmr.player.audio);
    },
    
    //Append the <audio> tag to the DOM
    outputTag : function() {
      gmr.player.audio.appendTo('body');
    },
    
    //Sets the callback for the onended event
    assignEndCallback : function(reference) {
      gmr.player.endCallback = reference;
      $(gmr.player.audio).bind('ended', gmr.player.endCallback());
    },
    
    //TODO: Find some way to handle "onended"
    
   
  }
}();
