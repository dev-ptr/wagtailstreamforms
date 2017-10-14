# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtailstreamforms.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField((('form', wagtail.wagtailcore.blocks.StructBlock((('form', wagtailstreamforms.blocks.FormChooserBlock()),))),))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]