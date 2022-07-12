:blogpost: true
:date: {{ cookiecutter.post_date }}
:category: Tech
:tags: Rust

{% set title_length = cookiecutter|length %}
{% set title_length = title_length + 10 %}
{% for characters in range(title_length+10) %}={%endfor%}
{{ cookiecutter.post_title }}
{% for characters in range(title_length+10) %}={%endfor%}
