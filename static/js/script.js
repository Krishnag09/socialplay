const video = document.getElementById('video');
let captureBtn;
let videoElement;
let socket;

window.onload = function () {
  socket = new WebSocket("ws://127.0.0.1:5000/communicate");

  socket.onopen = function (e) {
    console.log("[open] Connection established");
    console.log("Sending to server");

    socket.send(JSON.stringify({ name: 'Thimmu' }));
  };

  socket.onmessage = function (event) {
    console.log(`[message] Data received from server: ${event.data}`);
  };

  socket.onclose = function (event) {
    if (event.wasClean) {
      console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
    } else {
      // e.g. server process killed or network down
      // event.code is usually 1006 in this case
      console.log('[close] Connection died');
    }
  };

  socket.onerror = function (error) {
    console.log(`[error] ${error.message}`);
  };
}



Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('../../static/js/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('../../static/js/models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('../../static/js/models'),
  faceapi.nets.faceExpressionNet.loadFromUri('../../static/js/models')
]).then(ShowCapture)

function ShowCapture() {
  captureBtn = document.querySelector('#captureButton')
  captureBtn.style.display = 'block';
}

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}

function captureEmotion() {
  captureBtn.style.display = 'none';
  videoElement = document.querySelector('#videoElement');
  videoElement.style.display = 'block';
  startVideo();
}
let displaySize;
let canvas = null;
video.addEventListener('play', () => {
  if (!canvas) {
    canvas = faceapi.createCanvasFromMedia(video);
    document.body.append(canvas);
    displaySize = { width: video.width, height: video.height };
    faceapi.matchDimensions(canvas, displaySize);
    findEmotion();
  }
});

let emoInterval;
function findEmotion() {
  emoInterval = setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    // console.log(detections[0].expressions);
    dispEmotion(detections[0].expressions);
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    faceapi.draw.drawDetections(canvas, resizedDetections)
    faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
    // faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
  }, 100);
}
let emotionDisplayed = false;
let disp_emotion = '';
function dispEmotion(emotions) {
  // console.log(emotions);
  if (emotions && !emotionDisplayed) {
    emotionDisplayed = true;
    let max_confidence = 0;
    let keys = Object.keys(emotions);
    for (let emotion of keys) {
      if (emotions[emotion] > max_confidence) {
        disp_emotion = emotion;
        max_confidence = emotions[emotion];
      }
    }
    console.log(disp_emotion);
    document.querySelector('#emoResp').innerText = disp_emotion;
  }
}

function retry() {
  document.querySelector('#emoResp').innerText = '';
  emotionDisplayed = false;
  disp_emotion = '';
  clearInterval(emoInterval);
  findEmotion();
}



const musicContainer = document.getElementById('music-container');
const playBtn = document.getElementById('play');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');

const audio = document.getElementById('audio');
const progress = document.getElementById('progress');
const progressContainer = document.getElementById('progress-container');
const title = document.getElementById('title');
const cover = document.getElementById('cover');
const currTime = document.querySelector('#currTime');
const durTime = document.querySelector('#durTime');

function sendToBackend() {
  let toSend = { emotion: disp_emotion };
  socket.send(JSON.stringify(toSend));
  clearInterval(emoInterval);
  canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
  // var elem = document.querySelector('canvas');
  // elem.parentNode.removeChild(elem);
  canvas.remove();
  canvas = null;
  captureBtn.style.display = 'block';
  videoElement.style.display = 'none';
  document.querySelector('#emoResp').innerText = '';
  emotionDisplayed = false;
  disp_emotion = '';
}

