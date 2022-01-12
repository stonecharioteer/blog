# Stonecharioteer.com Blog

This is the jekyll source code for my blog. I use [YAMT](https://github.com/PandaSekh/Jekyll-YAMT)
for the layout and the themes.

This blog uses ablog and sphinx

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


## Local Testing

Just use the docker command:

```
docker run --rm -it \
  --volume="$PWD:/srv/jekyll" \
  --volume="$PWD/vendor/bundle:/usr/local/bundle" \
  -p 4000:4000 jekyll/jekyll:3.8 \
  jekyll serve
```
