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
    
    var audio = document.createElement('audio');
    
    //Add a <source> tag to <audio> tag with the src 'path'
    function addSource(path) {
      $('<source>').attr('src', path).appendTo('audio);
    }
    
    //TODO: Find some way to handle "onended"
   
  }
}
