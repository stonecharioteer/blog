:blogpost: true
:date: Jul 14, 2022
:category: Show and Tell
:tags: meta, blogging

.. _using-cookiecutter-to-create-a-blogpost-template:

====================================================================
Using Cookiecutter to Create a Blogpost Template
====================================================================

I've shifted my blog to use `ablog <>`_, a `sphinx <>`_ based static blog
generator because I love using ReStructuredText over Markdown, and my choices
for a platform that supports RST are limited. However, the tooling around Sphinx
and ablog in general are grim. I needed a way to create posts without messing up
the metadata at the top of the post.

To the curious, each RST based blog article looks like this at the top


.. code-block:: restructured-text

   :blogpost: true
   :date: Jul 14, 2022
   :category: Show and Tell
   :tags: meta, blogging

   .. _unique-identifier:

   ==========================================================================
   Post Title (the overline and underline need to be longer than the title)
   ==========================================================================

This header content is a composite of ablog's needs and my usage of sphinx's
features. The ``:blogpost:`` segments are frontmatter that is then used to
orchestrate the post. The ``.. _unique-identifier:`` is a sphinx-based tag for
that position in the file. I can later use this in a ``:ref:``block to create
hyperlinks. This is easier than trying to use some esoteric tagging system such
as the one
