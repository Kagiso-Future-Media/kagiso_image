# kagiso_image

[ ![Codeship Status for Kagiso-Future-Media/kagiso_image](https://codeship.com/projects/9aa7e3c0-0eb2-0134-ab88-0a3e61dce168/status?branch=master)](https://codeship.com/projects/156413)

A custom Wagtail image that has optional fields for:
- caption
- attribution
- alt_text

## Installation
`pip install kagiso_image`

Add `kagiso_image` to your `INSTALLED_APPS` in your `settings.py`.
Add `WAGTAILIMAGES_IMAGE_MODEL = 'kagiso_image.ImageWithAttribution'` to your `settings.py`.

`python manage.py migrate`

## Usage
```py
from kagiso_image.models import ImageWithAttribution


class MyPage(Page):
    my_image = models.ForeignKey(
        ImageWithAttribution,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='+'
    )
```

## Settings
```py
MIN_IMAGE_WIDTH = 100
MIN_IMAGE_HEIGHT = 100

# The above settings are only enforced if both are set!
# The values are None by default
```
