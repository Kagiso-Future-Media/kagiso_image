from django.conf import settings
import pytest

from ..constants import MIN_IMAGE_HEIGHT, MIN_IMAGE_WIDTH
from ..exceptions import ImageTooSmall
from ..utils import create_test_image


@pytest.mark.django_db
class TestImageWithAttribution:

    def test_correctly_sized_image_saves(self, tmpdir):
        settings.MEDIA_ROOT = str(tmpdir)

        result = create_test_image(MIN_IMAGE_WIDTH, MIN_IMAGE_HEIGHT)

        assert result.id
        assert result.width == MIN_IMAGE_WIDTH
        assert result.height == MIN_IMAGE_HEIGHT

    def test_incorrectly_sized_image_raises(self, tmpdir):
        settings.MEDIA_ROOT = str(tmpdir)

        with pytest.raises(ImageTooSmall):
            create_test_image(MIN_IMAGE_WIDTH - 1, MIN_IMAGE_HEIGHT - 1)
