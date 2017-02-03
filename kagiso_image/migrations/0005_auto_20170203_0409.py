# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 04:09
from __future__ import unicode_literals

from django.db import migrations
from wagtail.wagtailimages.utils import get_fill_filter_spec_migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kagiso_image', '0004_auto_20170202_0213'),
    ]

    forward, reverse = get_fill_filter_spec_migrations('kagiso_image', 'ImageWithAttributionRendition')
    operations = [
        migrations.RunPython(forward, reverse),
    ]
