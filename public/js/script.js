async function startCamera() {
    const constraints = { video: true };
    try {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        document.getElementById('camera-feed').srcObject = stream;
    } catch (error) {
        console.error('Error accessing camera:', error);
    }
}
startCamera();

const captureButton = document.getElementById('capture-button');
const capturedPhoto = document.getElementById('captured-photo');

captureButton.addEventListener('click', () => {
    const video = document.getElementById('camera-feed');
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    capturedPhoto.src = canvas.toDataURL('image/png');
    capturedPhoto.style.display = 'block';

    const dataUrl = canvas.toDataURL('image/png');
    const blob = dataURItoBlob(dataUrl);

    const formData = new FormData();
    formData.append('photo', blob);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error saving photo:', error);
    });
});

function dataURItoBlob(dataURI) {
    const byteString = atob(dataURI.split(',')[1]);
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }
    return new Blob([ab], { type: 'image/png' });
}
