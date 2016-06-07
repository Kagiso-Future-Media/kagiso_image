from django.conf import settings


MIN_IMAGE_WIDTH = getattr(settings, 'MIN_IMAGE_WIDTH', None)
MIN_IMAGE_HEIGHT = getattr(settings, 'MIN_IMAGE_HEIGHT', None)
