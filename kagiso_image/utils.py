from io import BytesIO

from django.core.files.images import ImageFile
from PIL import Image

from .models import ImageWithAttribution


def create_test_image(width=500, height=500):
    binary_stream = BytesIO()

    file_name = 'test_image.png'

    image = Image.new('RGB', (width, height), 'white')
    image.save(binary_stream, 'PNG')
    image_file = ImageFile(
        binary_stream,
        name=file_name
    )

    model_image = ImageWithAttribution(
        title=file_name,
        file=image_file
    )
    model_image.save()

    return model_image
