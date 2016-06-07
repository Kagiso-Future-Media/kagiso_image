from django.conf import settings
import pytest

from ..exceptions import ImageTooSmall
from ..utils import create_test_image


@pytest.mark.django_db
class TestImageWithAttribution:

    def test_correctly_sized_image_saves(self, tmpdir):
        settings.MEDIA_ROOT = str(tmpdir)
        width = 400
        height = 400

        result = create_test_image(width, height)

        assert result.id
        assert result.width == height
        assert result.height == height

    def test_incorrectly_sized_image_raises(self, tmpdir):
        settings.MEDIA_ROOT = str(tmpdir)
        width = 150
        height = 150

        with pytest.raises(ImageTooSmall) as e:
            create_test_image(width, height)
