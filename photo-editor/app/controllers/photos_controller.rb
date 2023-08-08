class PhotosController < ApplicationController
  def index
    render "photos/index"
  end

  def grayscale
    image = params[:image]

    @grayscale_image = Photo.grayscale(image)

    render "photos/grayscale"
  end
end
