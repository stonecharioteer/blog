from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

# from wagtailmarkdown.edit_handlers import MarkdownPanel
# from wagtailmarkdown.fields import MarkdownField

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        # MarkdownPanel("body"),
    ]
