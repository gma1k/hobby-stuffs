class Photo < ApplicationRecord
  def self.grayscale(image)
    img = Magick::ImageList.new(image)

    img = img.modulate(1.0, 0.0, 1.0)

    img.write("grayscale_#{image}")

    return "grayscale_#{image}"
  end
end
