
<script>
window.onload = function() {
document.getElementById('videoPopup').style.display = 'block';
}

document.getElementById('playButton').onclick = function() {
document.getElementById('myVideo').play();
}

document.getElementById('soundButton').onclick = function() {
document.getElementById('myVideo').muted = false;
}

document.getElementById('closeButton').onclick = function() {
var video = document.getElementById('myVideo');
video.pause();
video.currentTime = 0;
document.getElementById('videoPopup').style.display = 'none';
}
</script>
