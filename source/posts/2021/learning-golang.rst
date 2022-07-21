:blogpost: true
:date: Dec 28, 2021
:category: Learning
:tags: golang, tech, programming

=========================
Learning Golang
=========================

Despite my numerous failed attempts at learning golang, I've decided to bite the bullet and try yet again.
This time, `Learn Go With Tests <https://quii.gitbook.io/learn-go-with-tests>`_ is my favorite resource.

This is a great "book" that sticks to the principles of TDD with gusto (do people still say gusto?).
I'm having fun working on it and will have more thoughts later. I've already written more golang than I
ever have. I've tried A Tour of Golang before and never got around to finishing it. This seems much more
structured and might be my favorite new way of learning how to learn a programming language.

To help me measure my journey, I'm going to target being able to do the following things:

1. Command Line Application

   * Do what I'm able to in Python using Click
   * Read a TOML file for config
   * Use whatever is the equivalent of Pathlib to find ``~/.config/APPNAME/default.toml``
   * Read environment variables to get custom settings files.
   * Read environment variables to get overrides for custom settings

2. Interact with an API

   * Create a CLI (again) which interacts with some public API (Maybe the Starwars or Pokemon API)
   * Find the equivalent of ``retrying`` to backoff from requests.
   * Find out how to pass Authentication headers/tokens
   * Multiprocessing? Goroutines?

3. Create a REST API

   * Create a simple HTTP API
   * Write to SQL Lite
   * Write to Redis
   * Write to RabbitMQ
   * How would I do background tasks?

For now, this is all I want to achieve learning Golang. I think the CLI part takes higher precedence since
I mostly write CLIs. I'd like to see if I am able to shift to Golang for everything I do at work.
