project = "stonecharioteer.com"
copyright = "2022, Vinay Keerthi"
author = "Vinay Keerthi"
extensions = [
    "sphinx.ext.todo",
    # "sphinx_design",
    "sphinx.ext.githubpages",
    "sphinx_panels",
    "sphinxcontrib.youtube",
    "notfound.extension",
    # "sphinx_last_updated_by_git",
    "yasfb",
]
templates_path = ["_templates"]
exclude_patterns = ["_drafts/**"]
html_theme = "furo"
html_title = "Stonecharioteer"
serif_fonts = "Newsreader, Garamond, Helvetica, Times New Roman, Serif"
html_theme_options = {
    "light_css_variables": {
        "font-stack": serif_fonts,
        "font-size": 16
    },
    "light_logo": "images/logo/stonecharioteer-banner.png",
    "dark_logo": "images/logo/stonecharioteer-banner-bnw.png",
    "dark_css_variables": {
        "font-stack": serif_fonts,
        "font-size": 16
    },
}
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_last_updated_fmt = "%b %d, %Y"
html_permalinks = True
todo_include_todos = True
html_show_sphinx = False

feed_base_url = "https://stonecharioteer.com"
feed_author = author
notfound_urls_prefix = None

html_meta = {
    'property="og:image"': 'https://stonecharioteer.com/_static/images/logo/stonecharioteer-banner.png',
    'name="twitter:image"': 'https://stonecharioteer.com/_static/images/logo/stonecharioteer-banner.png',
} 
