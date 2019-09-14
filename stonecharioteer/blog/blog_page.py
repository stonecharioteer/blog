#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Blog post page model"""
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


class BlogPageTag(TaggedItemBase):
    """Enable tags
    using https://docs.wagtail.io/en/v2.5/reference/pages/model_recipes.html#tagging
    as an example"""
    content_object = ParentalKey(
        'blog.BlogPage', on_delete=models.CASCADE,
        related_name="tagged_items")


class BlogPage(Page):
    """Individual blog post page."""
    template = "blog/blog_page.html"
    date = models.DateField("Post date")
    intro = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body", classname="full")
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel("tags")
    ]

    class Meta:
        """Metadata Class
        Implement this to explicitly set the metadata."""
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
