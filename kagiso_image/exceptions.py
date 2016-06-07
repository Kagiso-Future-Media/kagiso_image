from .constants import MIN_IMAGE_HEIGHT, MIN_IMAGE_WIDTH


class ImageTooSmall(Exception):

    def __init__(self, image):
        self.image = image
        self.message = ('{0} is too small ({1} x {2}).'
                        'It should be a minimum of {3} x {4}').format(
                            image.file, image.width, image.height,
                            MIN_IMAGE_WIDTH, MIN_IMAGE_HEIGHT
        )
