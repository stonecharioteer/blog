#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Blog Index Page"""

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index


class BlogIndexPage(Page):
    """Blog index served at /blog"""
    template = "blog/blog_index_page.html"
    max_count = 1

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

    def serve(self, request):
        """Serve list of blog posts"""
        from django.shortcuts import render
        from .blog_page import BlogPage
        blogs = BlogPage.objects.child_of(self).live()
        # blogs = self.get_children().live().order_by("-first_published_at")

        tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__name=tag)

        return render(request, self.template, {
            'page': self,
            'blogpages': blogs,
        })
