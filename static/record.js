window.URL = window.URL || window.webkitURL;
navigator.getUserMedia = 
  navigator.getUserMedia||
  navigator.webkitGetUserMedia ||
  navigator.mozGetUserMedia ||
  navigator.msGetUserMedia;
var video = document.querySelector('video');
var cameraStream = '';
if(navigator.getUserMedia){
  navigator.getUserMedia(
    {audio: false, video:true},
    function(stream){
      cameraStream = stream;
      video.src = window.URL.createObjectURL(stream);
    },
    function(){
      document.writeln("problem with accessing the hardware!");
    }

  );
} else {
  document.writeln("video caputer is not supported!");
}

document.querySelector('#stopbt').addEventListener(
  'click',
  function(e){
    video.src='';
    cameraStream.stop();
  }
);