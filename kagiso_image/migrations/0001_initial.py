# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import wagtail.wagtailadmin.taggable
import wagtail.wagtailimages.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailimages', '0008_image_created_at_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageWithAttribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('file', models.ImageField(verbose_name='File', height_field='height', width_field='width', upload_to=wagtail.wagtailimages.models.get_upload_to)),
                ('width', models.IntegerField(verbose_name='Width', editable=False)),
                ('height', models.IntegerField(verbose_name='Height', editable=False)),
                ('created_at', models.DateTimeField(verbose_name='Created at', auto_now_add=True, db_index=True)),
                ('focal_point_x', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_y', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_width', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_height', models.PositiveIntegerField(blank=True, null=True)),
                ('file_size', models.PositiveIntegerField(editable=False, null=True)),
                ('attribution', models.CharField(max_length=255, blank=True, null=True)),
                ('alt_text', models.CharField(max_length=255, blank=True, null=True)),
                ('caption', models.CharField(max_length=255, blank=True, null=True)),
                ('tags', taggit.managers.TaggableManager(help_text=None, verbose_name='Tags', to='taggit.Tag', blank=True, through='taggit.TaggedItem')),
                ('uploaded_by_user', models.ForeignKey(editable=False, null=True, verbose_name='Uploaded by user', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, wagtail.wagtailadmin.taggable.TagSearchable),
        ),
        migrations.CreateModel(
            name='ImageWithAttributionRendition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('file', models.ImageField(height_field='height', width_field='width', upload_to='images')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(editable=False, default='', blank=True, max_length=255)),
                ('filter', models.ForeignKey(related_name='+', to='wagtailimages.Filter')),
                ('image', models.ForeignKey(related_name='renditions', to='kagiso_image.ImageWithAttribution')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='imagewithattributionrendition',
            unique_together=set([('image', 'filter', 'focal_point_key')]),
        ),
    ]
