# kagiso_image
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
