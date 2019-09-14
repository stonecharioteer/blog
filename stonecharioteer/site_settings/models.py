#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""SocialMediaSettings
"""

from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
    """Social Media settings"""

    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    github = models.URLField(blank=True, null=True, help_text="Github URL")
    gitlab = models.URLField(blank=True, null=True, help_text="Gitlab URL")
    youtube = models.URLField(blank=True, null=True, help_text="Youtube URL")
    pypi = models.URLField(blank=True, null=True, help_text="PyPI URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("twitter"),
            FieldPanel("github"),
            FieldPanel("gitlab"),
            FieldPanel("youtube"),
            FieldPanel("pypi"),
        ], heading="Social Media Settings")
    ]
