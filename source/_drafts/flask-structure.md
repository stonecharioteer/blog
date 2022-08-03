---
title: Building a Multipage Application with Flask and Dash
layout: post
date: 2020-07-17T15:20:26.511Z
categories: [flask, python]
description: "A way to use flask and dash together, with patterns and best practises."
customexcerpt: "I have been following a bunch of practises to use Flask and Dash together to build web applications, and I wanted to document them for others to understand and improve upon."
---


## Prerequisites

This is an *intermediate* to *advanced* article on `flask` and `dash`,
and before you begin reading this, I would recommend understanding both those libraries to some extent. Here are my favourite resources on these:

1. Miguel Grinberg's Flask Mega-Tutorial
2. Explore Flask
3. Plotly Dash Documentation

If you are familiar with `flask` and not `dash`, read the documention, and know that `dash` offers you a way to build web pages in Python. It is largely sold as dashboarding framework, but underneath, it converts your Python code into `react` code. You *do not* need to know any `reactjs` or javascript to understand this post.

## Introduction

I have been using `flask` for quite some time. It is my framework of choice, and I can be very opinionated about this. However, I like `django`'s way of configuring an application, and through reading resources that have shown me how to setup a `flask` app for production purposes, I make it a point to follow this application structure.

All the work in this article will be documented in this repository.

If you are interested in a video tutorial for flask, I have previously taken a workshop with the Bangalore Python Meetup Group on Flask. That is a very beginner-level workshop, and this seeks to address productionizing flask, as well as integrating multipage views with `dash`.


## Setup.

1. Clone this repository.

```
git clone flask-dash-multipageapp-tutorial
cd flask-dash-multipage-app-tutorial
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Structure

This application is structured completely around having something that
can be packaged, if needed, and used elsewhere.

The folder structure is as follows:
```
```

## Cookiecutter Template

Finally, since I do this setup each time I have a multipage application
that I build using this approach, I made myself a cookiecutter template that you can use (and contribute to!)

```
cookiecutter gh:stonecharioteer/cookiecutter-dash-multipage.git
```

This also adds `jwt`-based authentication optionally, should you wish it.


