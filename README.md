# Stonecharioteer.com Blog

This is the jekyll source code for my blog. I use [YAMT](https://github.com/PandaSekh/Jekyll-YAMT)
for the layout and the themes.

## Snippet for Title Block for markdown files

```javascript
{
    "titleblock": {
        "prefix": "title",
        "body": [
            "---",
            "title: $1",
            "layout: post",
            "categories: [$2]",
            "image: /assets/images/posts/$3",
            "description: \"$4\"",
            "customexcerpt: \"$5\"",
            "---"
        ]
    },
    "admonition": {
        "prefix": "note",
        "body": [
            "{% capture value%}",
            "$1",
            "{% endcapture%}",
            "{% include note.html title=\"$2\" alert_type="${3|note,warning,info}" content=value %}",
            "",
            "",
        ]
    }
}
```

This blog is accessible at [www.stonecharioteer.com](www.stonecharioteer.com).
