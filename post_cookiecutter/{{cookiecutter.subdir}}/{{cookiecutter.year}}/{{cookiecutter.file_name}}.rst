:blogpost: true
:date: {{ cookiecutter.post_date }}
:category: {{cookiecutter.category}}
:tags:
{% set title_length = cookiecutter|length %}{% set title_length = title_length + 10 %}
.. _{{cookiecutter.file_name}}:

{% for characters in range(title_length+10) %}={%endfor%}
{{ cookiecutter.post_title }}
{% for characters in range(title_length+10) %}={%endfor%}
