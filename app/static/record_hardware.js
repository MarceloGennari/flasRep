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
var send = true;
var numberScreenshots = 0;

function upload() {
  var dt = canvas.toDataURL('image/jpeg');
  dt = dt.substr(23);
    $.ajax({
      type: "POST",
      url: "/hardware",
      data: { 
        scnumb: numberScreenshots,
        imgBase64: dt
      }
    }).done(function(o) {
      console.log('saved');
      console.log(o);
      $('#output').html(o);

        if(o!="unknown"){
        $('#aud').attr("src", 'static/audios/roll.wav');
        $('#aud').get(0).load();
        $('#aud').get(0).play();
        $('#aud').attr("src", '');
        }
      }
    );
    numberScreenshots = numberScreenshots+1;
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
        if(send){
          drawFromVideo();
          upload();
        }
      }, 3000);
    },
    function(){
      document.writeln("Problem accessing the camera, please check your permissions");
    }
  );
} else {
  document.writeln("No camera detected");
}

document.querySelector('#stopbt').addEventListener(
  'click',
  function(e){
    video.src='';
    send = false;
  }
);
