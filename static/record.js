window.URL = window.URL || window.webkitURL;
navigator.getUserMedia = 
  navigator.getUserMedia||
  navigator.webkitGetUserMedia ||
  navigator.mozGetUserMedia ||
  navigator.msGetUserMedia;
var video = document.querySelector('video');
var cameraStream = '';
var canvas= document.querySelector('canvas');
var ctx = canvas.getContext('2d');

function upload() {
  var dt = canvas.toDataURL('image/jpeg');
  dt = dt.substr(23);
  $.ajax({
    type: "POST",
    url: "/video",
    data: { 
      imgBase64: dt
    }
  }).done(function(o) {
    console.log('saved'); 
    // If you want the file to be visible in the browser 
    // - please modify the callback in javascript. All you
    // need is to return the url to the file, you just saved 
    // and than put the image in your browser.
  });
};

function drawFromVideo(){
  ctx.fillRect(0, 0, 480, 360);
  ctx.drawImage(video, 0, 0, 480, 360);
  var img = canvas.toDataURL("imgScreenshot.jpg");
};

if(navigator.getUserMedia){
  navigator.getUserMedia(
    {audio: false, video:true},
    function(stream){
      cameraStream = stream;
      video.src = window.URL.createObjectURL(stream);

      setInterval(function() {
        drawFromVideo();
        upload();
      }, 3000);
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
