---
title: Building Single Page Applications in React using Dash and Python
layout: post
categories: [python, react, learning]
description: "How to build Single Page web applications without any Javascript"
customexcerpt: "The `dash` library from Plotly allows you to build webpages that internally serve React components. Let's see how to use this to build a SPA with authentication, multiple pages and **zero** Javascript."
---

## Introduction

Dash is a Python library from Plotly that helps you take graphs that are generated using Plotly and then convert them
into a web page.

In simple terms, Dash does just this. However, what Dash does internally is take your Python objects that define
your views and convert them into React components. This is a powerful way of building React applications without
having to write your own React code.

Dash also uses Flask internally, converting all your function calls into Flask API calls. This makes it easy to decouple
the application and build a full stack application purely in Python.

Note that by saying we are writing Python for the UI, I don't mean that we are using WASM. This approach has nothing
to do with Web Assembly. Instead, it is a simpler way to just take Python code and generate Javascript.

## Prerequisites

To understand this article, you should have an understanding of the following items.

1. Python: Learn how decorators work, how to write class definition and how methods are called.
2. Flask: Go through a good tutorial on flask. You will need to understand blueprints, the Application factory method approach, and MethodViews.
3. Plotly: Some minor understanding of the Plotly library is required.
4. HTML and CSS: While JS is not required to build your own Dash apps, I'd recommend getting to learn as much HTML and CSS as you can since that will help you polish your application.

Resources for all these can be found at the end of this article.

## Setup and Installation

## Structure of the Application

### Flask Structure

### Dash Structure

## Testing the Application

### Testing the Utilities


### Testing the Flask API

### Testing the Dash UI with Selenium

#### Note on User Acceptance Tests

## Dash Callbacks

## Deployment

### Using `systemctl` and `gunicorn`

### Using `docker`


#### Using `docker-compose`

### Using Kubernetes

#### Pushing Updates to Settings

## Using the cookiecutter Template

## End Note

## References

1. [Python 101: Classes](https://python101.pythonlibrary.org/chapter11_classes.html)
2. [Python 101: Decorators](https://python101.pythonlibrary.org/chapter25_decorators.html?highlight=decorator)
3. [Real Python Article on Decorators](https://realpython.com/primer-on-python-decorators/)
4. [Real Python article on Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)
5. [Miguel Grinberg's Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
6. [Explore Flask](https://exploreflask.com/en/latest/)
7. [Flask `create_app` example](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/)
8. [Plotly Documentation](https://plotly.com/python/)
9. [Dash documentation](https://dash.plotly.com/)
10. [Pytest Documentation](https://docs.pytest.org/en/latest/contents.html)
11. [Gunicorn Documentation](https://gunicorn.org/)
12. [How to write a `systemctl` file](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-centos-7)
13. [Docker tutorial](https://docs.docker.com/)
14. [Docker Flask tutorial](https://github.com/docker/labs/tree/master/beginner/flask-app)
15. [Docker Compose tutorial](https://docs.docker.com/compose/)
16. [k3s documentation](https://k3s.io/)
17. [Flask on k8s](https://testdriven.io/blog/running-flask-on-kubernetes/)
