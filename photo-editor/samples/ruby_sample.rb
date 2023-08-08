require 'RMagick'

def grayscale(image)
  # Create an ImageMagick object from the image file
  img = Magick::ImageList.new(image)

  # Apply the grayscale filter
  img = img.modulate(1.0, 0.0, 1.0)

  # Save the modified image to a file
  img.write("grayscale_#{image}")
end
