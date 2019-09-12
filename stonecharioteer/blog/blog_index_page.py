#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Blog Index Page
"""

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index


class BlogIndexPage(Page):
    """Blog index served at /blog"""
    template = "blog/blog_index_page.html"
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full")
    ]

    class Meta:
        """Meta Data class
        This class explicitly sets the metadata"""
        verbose_name = "Blog Index Page"
        verbose_name_plural = "Blog Index Pages"


    def get_context(self, request):
        """Modify QuerySet by implementing get_context
        Use this method to update the context to only
        include the published posts,
        in reverse-chronological-order"""
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by("-first_published_at")
        context["blogpages"] = blogpages
        return context


class BlogPage(Page):
    """Individual blog post page."""
    template = "blog/blog_page.html"
    date = models.DateField("Post date")
    intro = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body", classname="full")
    ]

    class Meta:
        """Metadata Class
        Implement this to explicitly set the metadata."""
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
