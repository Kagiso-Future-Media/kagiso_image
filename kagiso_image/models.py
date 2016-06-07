from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from wagtail.wagtailimages.models import (
    AbstractImage,
    AbstractRendition,
    Image,
)

from .exceptions import ImageTooSmall


class ImageWithAttribution(AbstractImage):
    attribution = models.CharField(max_length=255, blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)

    admin_form_fields = Image.admin_form_fields + (
        'attribution',
        'alt_text',
        'caption',
    )

    @property
    def full_url(self):
        return self.get_rendition('original').url

    def save(self, *args, **kwargs):
        if not self.id:
            if self.width < 350 or self.height < 350:
                raise ImageTooSmall(self)

        super().save(*args, **kwargs)


class ImageWithAttributionRendition(AbstractRendition):
    image = models.ForeignKey(ImageWithAttribution, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter', 'focal_point_key'),
        )


# Delete the source image file when an image is deleted
@receiver(pre_delete, sender=ImageWithAttribution)
def image_delete(sender, instance, **kwargs):
    instance.file.delete(False)  # pragma: no cover


# Delete the rendition image file when a rendition is deleted
@receiver(pre_delete, sender=ImageWithAttributionRendition)
def rendition_delete(sender, instance, **kwargs):
    instance.file.delete(False)  # pragma: no cover
