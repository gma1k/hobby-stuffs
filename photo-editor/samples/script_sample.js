var rotateButton = document.getElementById("rotate-button");

var imageCanvas = document.getElementById("image-canvas");
var imageContext = imageCanvas.getContext("2d");

var image = new Image();
image.src = "https://example.com/image.jpg";

image.onload = function() {
  imageContext.drawImage(image, 0, 0, imageCanvas.width, imageCanvas.height);
};

var angle = 0;

rotateButton.addEventListener("click", function() {
  angle += 90;

  imageContext.clearRect(0, 0, imageCanvas.width, imageCanvas.height);

  imageContext.save();

  imageContext.translate(imageCanvas.width / 2, imageCanvas.height / 2);

  imageContext.rotate(angle * Math.PI / 180);

  imageContext.drawImage(image, -image.width / 2, -image.height / 2);

  imageContext.restore();
});
