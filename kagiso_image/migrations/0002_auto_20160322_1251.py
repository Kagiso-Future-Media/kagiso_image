# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.models
import taggit.managers
import wagtail.wagtailcore.models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('kagiso_image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagewithattribution',
            name='collection',
            field=models.ForeignKey(related_name='+', verbose_name='collection', default=wagtail.wagtailcore.models.get_root_collection_id, to='wagtailcore.Collection'),
        ),
        migrations.AlterField(
            model_name='imagewithattribution',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at', db_index=True),
        ),
        migrations.AlterField(
            model_name='imagewithattribution',
            name='file',
            field=models.ImageField(upload_to=wagtail.wagtailimages.models.get_upload_to, height_field='height', verbose_name='file', width_field='width'),
        ),
        migrations.AlterField(
            model_name='imagewithattribution',
            name='height',
            field=models.IntegerField(editable=False, verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='imagewithattribution',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, through='taggit.TaggedItem', verbose_name='tags', to='taggit.Tag', help_text=None),
        ),
        migrations.AlterField(
            model_name='imagewithattribution',
            name='title',
            field=models.CharField(verbose_name='title', max_length=255),
        ),
        migrations.AlterField(
            model_name='imagewithattribution',
            name='uploaded_by_user',
            field=models.ForeignKey(blank=True, verbose_name='uploaded by user', to=settings.AUTH_USER_MODEL, null=True, editable=False, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AlterField(
            model_name='imagewithattribution',
            name='width',
            field=models.IntegerField(editable=False, verbose_name='width'),
        ),
    ]
