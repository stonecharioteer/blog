#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""About Page
"""

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class AboutPage(Page):
    """About Page"""
    template = "home/about.html"
    max_count = 1

    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full")
    ]

    class Meta:
        """Metadata class
        This class is used to explicitly set the metadata"""
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
