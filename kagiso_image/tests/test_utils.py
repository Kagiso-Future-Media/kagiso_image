from django.conf import settings
import pytest

from ..constants import MIN_IMAGE_HEIGHT, MIN_IMAGE_WIDTH
from ..utils import create_test_image


@pytest.mark.django_db
def test_create_test_image(tmpdir):
    settings.MEDIA_ROOT = str(tmpdir)

    result = create_test_image(MIN_IMAGE_WIDTH, MIN_IMAGE_HEIGHT)

    assert result.width == MIN_IMAGE_WIDTH
    assert result.height == MIN_IMAGE_HEIGHT
