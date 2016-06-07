class ImageTooSmall(Exception):

    def __init__(self, image):
        self.image = image
        self.message = ('{0} is too small ({1} x {2}).'
                        'It should be a minimum of 350 x 350').format(
                            image.file, image.width, image.height
        )
