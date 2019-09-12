#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Home page class definition
"""

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    """Home page class definition"""
    template = "home/home.html"
    max_count = 1

    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        """Metadata class
        This class is used to explicitly set the metadata.
        """
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
