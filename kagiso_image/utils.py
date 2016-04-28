from io import BytesIO

from django.core.files.images import ImageFile
from faker import Faker
from PIL import Image

from .models import ImageWithAttribution


def create_test_image():
    faker = Faker()
    binary_stream = BytesIO()

    file_name = faker.file_name(extension='png')

    image = Image.new('RGB', (640, 480), 'white')
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
