.. post::
   :tags: draft, oso, authorization, web-development, tech
   :category: Tutorial
   :redirect: oso-authz

======================================
Authorization in Python using Oso
======================================

--------
Outline
--------

1. Prelude
2. Introduction
3. What is Oso?
4. Why do I need Oso?
5. Hello Oso
    1. What is Going On?
    2. What Happened?
    3. What if I want to *deny* access?
6. Oso in a CLI
    1. With argparse
    2. Write your own decorator for Click
7. Where is the Server?
8. Oso and Flask
    1. With a barebones Flask application
    2. Using flask-oso
    3. With Flask-Login
    4. With ``flask_jwt_extended``
9. Advanced Patterns
10. Getting Help
11. Cookiecutter Template

.. todo::
    * Explain how to use Oso with Argparse
    * Explain how to use Oso with Click
    * Explain how to use Flask-Oso
    * Explain how to use Oso with Flask Login
    * Explain how to use Oso with JWT Tokens
    * Explain how to use Oso with OIDC
    * Explain how to use the new ``resource`` fields.

----------
Prelude
----------

This is an article I've been working on for almost a year now. Life got in the way,
but it wasn't just that. I haven't been using Oso in the months since February,
since I've moved on to another company, but the central premise that excites
me about the library hasn't changed. The fun folks at Oso reached out to me
since I've been telling them about this article, and we had a fun chat about
it and how I've used Oso in a very non-conventional way at my previous
workplace. I am not affiliated with them or with my previous organization
at the time of this writing, and I'm not speaking for them, but I'll say this.
*Oso is darn good software*.

The structure of this post is to serve not as a tutorial to Oso. The official
[documentation](https://docs.osohq.com) more than serve that purpose. Instead,
I wanted to dig into *why* I find this library fascinating enough to be *this*
excited. I'm writing about all the different ways in which you *could* use Oso,
even if it wasn't exactly meant for that purpose. Not everyone will have such a
requirement, but in my opinion, this is how you learn. You build things that
might not see mobvious from the first glance. I'll save the fanboyism for the
conclusion, but I'll leave you with this.

While Oso does a lot for you under the hood, it's *what you can do* if you know
it like a power user that empowers you.

-----------------
Introduction
-----------------

Auth is one of the more underrated features in software. Not only is it hard
to do in a secure manner, it is also seldom appreciated when it is done well.
When auth works, it's business as usual, and when it doesn't, someone messed
up.

When people say **auth**, they could mean one of two things: *authentication*
(AuthN), or, *authorization* (AuthZ).

*Authentication* deals with user identity. Is user ``abc`` who they say they are?
It deals with user IDs and passwords and validation. It could additionally deal
with user tokens, sessions, and cookies among other things.

*Authorization* deals with a user's permissions. Is user ``abc`` *allowed* to do
the thing they have requested? Where are the authorization rules?  Who is
allowed to use this portion of your application? Who is denied it?

This article deals with *authorization* and not **authentication.**

When a developer goes about looking for a way to configure authorization, they
usually arrive at *roles*. A user's *role* is assigned certain permissions, and
if you need your user to be able to do something, then just add him to that
role. Easy-peasy.

There is a problem with this approach. The roles have to be checked in your
code, time and again. Want to add a new feature only admins with *cat* in their
username can perform on every third Sunday? Tough luck, you can't do that.

Or maybe you can.

---------------
What is Oso?
---------------

[Oso](https://osohq.com) is a library that takes care of authorization. In
coding terms, ``oso`` allows you to take code that looks like this:

.. code:: python
    :linenos:

    def user_can_do_this(user):
        if user.is_admin and user.id in ["abc","xyz", "lkjh"]:
            return True
        else:
            return False

    if user_can_do_this(user):
        print("I can do this!")
    else:
        print("Access denied!")

And rewrite it like this:

.. code:: python
    :linenos:

    if oso.is_allowed(user, "can_do", this):
        print("I can do this!")
    else:
        print("Access denied!")

And in your rules, you define this:

.. code::

    allow(user, "can_do", this) if user.is_admin and user.id in ["abc","xyz", "lkjh"]

For now, ignore what is inside the ``allow`` line. Indeed, also ignore the
*words* ``user``, ``"can_do"`` and ``this.`` *None of them have any meaning beyond*
*what you assign it in your code*.

Take a minute to reread the above two lines. This is important.

In an earlier paragraph, I used the term "words" to refer to ``user``, ``"can_do"``
and ``this.`` That was a gross over-simplification of what's happening here.
These are **tokens**.  The tokens do not have any real meaning as to what they
do. It is up to *you* to impart meaning to them.

While this doesn't look like much, it actually is. Oso provides users the
Polar declarative language with which to declare *policies* for the
application.

These policies enable developers to abstract the actual rules of authorization
and instead focus on their code. Everything else is denied to the user.

Yes, ``oso`` is *deny by default*. No one gets to do anything if you haven't
defined a rule that you're attempting to use.

## Why do I need Oso?

If you're used to doing things with *if* statements, or perhaps modular
decorators if you're in a Python world, and that's a good pattern to have, why
would you need ``oso``?

1. Oso does modularization for you.
2. You can use the Polar language syntax to define rules in a simple way.
3. You can hot load policies on the fly, meaning you can come up with runtime
   policies that you couldn't do without considerable effort.
4. Oso also gives you plugins for your favorite languages: You can reuse
   your policies *across* your organization: in *multiple* languages.
5. You can separately version control your policies.
6. Policies are just strings. You can store them in a database, if you want
   to. Also, [/r/madlads](https://reddit.com/r/madlads) is :point_right: that
   way.

--------------
Hello Oso
--------------

.. note:: Using Oso in other languages

    Oso supports several languages, not just Python. I use Python here merely for
    demonstrative purposes, but you should visit their official [documentation
    website](https://docs.osohq.com) to find more libraries supporting other
    languages such as Java, Rust and Node.js.


So how _do_ you use Oso in your python code?

First, install the library. (Make sure you're doing this in a virtual
environment for your project.)

.. code-block:: bash

    pip install oso

Then, create a [new python file.](https://github.com/stonecharioteer/blog/tree/master/code/oso-examples)

.. code-block:: python
    :linenos:

    from oso import Oso

    oso_object = Oso()

    oso_object.load_str("""allow("user", "can_use", "this_program");""")

    if oso_object.is_allowed("user", "can_use", "this_program"):
        print("Hello from oso")
    else:
        print("Access denied")

All examples from this post are available [here as a Github repository.](https://github.com/stonecharioteer/blog/tree/master/code/oso-examples)

What's Going On?
=================

The Oso documentation begins users with showing how you can integrate Oso
into a web application written in native Python. However, I believe in a first
principles approach.

In this example, we're loading the ``oso`` library, and then immediately creating
an instance of the ``oso.Oso`` class. This enables us to then bind *policies* to
the object.

A policy is declared in a language known as Polar. Polar takes inspiration from
Prolog, and I like to think of its rule system as a paradigm you'd find in
Rust's pattern matching. Don't let any of this intimidate you: I'll get to it
later. For now, all you need to know is that we've added the _line_
``allow("user", "can_use", "this_program");`` to the policies in the ``oso_object``
object.

.. tip:: Use double quotes for strings in Polar
    I've used triple double-quotes ``"""`` because Polar uses only double quotes
   ``"`` for its strings and I didn't want to use single-quotes ``'`` to surround
   them in Python. You may choose to do so if you like.


This line says:

> If a function called ``allow`` is triggered with 3 variables equal to,
> *literally*: ``"user"``, ``"can_use"`` and ``"this_program"``, then evaluate to
> ``true.`` (Polar uses ``true``/``false`` as booleans).

Next, we use this policy in our script, with ``oso_object.is_allowed.`` Note that
the arguments to ``is_allowed`` are *exactly* the same as those to ``allow.``

Oso's ``is_allowed`` looks for a function called ``allow`` loaded into the object
which has a matching pattern. (Again, don't worry too much about this for now.)
And it finds the single policy we have defined and realizes that the policy
matches and evaluates to ``True`` (this is on the Python side).

Hence, the line ``print("Hello from oso")`` works.

What Happened?
----------------

Under the hood, Oso evaluates Polar rules and loads them into the ``oso.Oso``
object that we create. Those rules dictate the outcome of
``oso_object.is_allowed`` calls. But here's a question for you:

Where are the rules coming from?

Polar is a declarative language. While it supports things like integers and
some rudimentary math, strings and boolean values, it doesn't have much else.

So what is ``allow``?

The interesting thing about ``oso`` and its choice with Polar is that ``allow`` is
whatever you want it to be.

Let me reiterate.

.. code-block::

    allow("user", "can_use", "this_program");

This *defines* a policy called ``allow`` with those **exact**: parameters.

``is_allowed`` matches its arguments with this policy, and realizes that it
matches the rule, thus evaluating to ``True`` in the Python file. ``is_allowed``
is *hard-wired* to find a declarative function named ``allow`` in all the polar
definitions that are *loaded* into memory at this current moment.

### What if I want to *deny* access?

That's simple. Just try to call ``is_allowed`` with **anything** else.

In our previous file, add the following:

.. code-block:: python
    :linenos:

    if oso_object.is_allowed("user-123", "can_run", "this_program"):
        print("Hello again, but you probably can't run this line.")
    else:
        print("You weren't authorized by the rules!")

This ``is_allowed`` will evaluate to ``False``, since it doesn't match the rule
that we've loaded into the ``oso_object.``

Remember what I've been saying about *pattern-matching*? Well, Oso looks for
an *exact* match for the rules. You *could* generalize it further by using types,
or your own classes, but we'll get to that later.

For now, you need to just understand that ``oso`` essentially does a 1:1 match
with the rules in your ``oso_object`` and evaluates ``is_allowed`` based on a
suitable ``allow`` policy.

-----------------
Oso in a CLI
-----------------

An interesting exercise to understand what you could do with Oso is to try building
a command line tool.

Using argparse
================

Let's write a quick CLI using ``argparse``:

.. code-block:: python
    :linenos:

    import argparse

    parser = argparse.ArgumentParser(
        description="Simple rmdir clone command-line-tool to demonstrate Oso's usage")
    parser.add_argument('path', metavar="P", type=str, help="Path to remove")


    if __name__ = "__main__":
        args = parser.parse_args()
        print(f"Attempting to remove directory: {args.path}.")

This is a simple CLI that uses
[``argparse``](https://docs.python.org/3/library/argparse.html). I'm going to
attempt a check to see if the user has write permissions, and only then allow a
delete.

Let's add some more code here.

.. code-block:: python
    :linenos:

    from enum import Enum

    class PathAttributes(Enum):
        """A bunch of enums to help understand the path attributes"""
        # path isn't a directory
        NOTADIRECTORY = 1
        # path is a writable directory
        WRITABLEDIRECTORY = 2
        # path is a read only directory (current user doesn't have write access)
        READONLYDIRECTORY = 3
        # path is an inaccessible directory (current user doesn't have read or write access)
        INACCESSABLEDIRECTORY = 4
        # path does not exist
        NONEXISTENTDIRECTORY = 5


    def get_path_attributes(path):
        """Returns a tuple of path attributes"""
        import pathlib
        import stat

        path = pathlib.Path(path)
        if not path.exists():
            return PathAttributes.NONEXISTENTDIRECTORY
        elif not path.is_dir():
            return PathAttributes.NOTADIRECTORY
        else:
            # this is a directory. We need to determine whether it's
            # writable, readable or accessible.
            path_stat_mode = path.stat().st_mode
            is_writeable = stat.S_ISWUSER(path_stat_mode) or stat.S_ISWGRP(path_stat_mode) or stat.S_ISWOTH(path_stat_mode)
            if is_writeable:
                return PathAttributes.WRITEABLEDIRECTORY
            else:
                is_readable = stat.S_ISRUSER(path_stat_mode) or stat.S_ISRGRP(path_stat_mode) or stat.S_ISROTH(path_stat_mode)
                if is_readable:
                    return PathAttributes.READONLYDIRECTORY
                else:
                    return PathAttributes.INACCESSIBLEDIRECTORY


    def rmdir(path):
        import shutil
        import oso
        path_attributes = get_path_attributes(path)
        if oso.is_allowed("can_remove", path_attributes):
            shutil.rmtree(path)
        else:
            raise PermissionError(f"You cannot delete {path}")

The above code looks like it is a lot. Let's take a moment to understand what is
happening here.

.. code-block:: python
     from enum import Enum


This imports the ``Enum`` class so that we can define an enumeration for the path
attributes. Take a moment to go through the
[official Python documentation on Enums](https://docs.python.org/3/library/enum.html)
if you've never used them before.

.. code-block:: python
    :linenos:

    class PathAttributes(Enum):
        """A bunch of enums to help understand the path attributes"""
        # path isn't a directory
        NOTADIRECTORY = 1
        # path is a writable directory
        WRITABLEDIRECTORY = 2
        # path is a read only directory (current user doesn't have write access)
        READONLYDIRECTORY = 3
        # path is an inaccessible directory (current user doesn't have read or write access)
        INACCESSABLEDIRECTORY = 4
        # path does not exist
        NONEXISTENTDIRECTORY = 5

The ``PathAttributes`` class defines an enumerated set of attributes for a folder.
The in-line comments explain what they're for.

At this point experienced pythonistas may be wondering what the heck I'm doing.
Bear with me, this isn't a best-principles-python-tutorial. It's a "what can
Oso do?" showcase.

Next, the functions:

.. code-block:: python
   :linenos:

    def get_path_attributes(path):
        """Returns a tuple of path attributes"""
        import pathlib
        import stat

        path = pathlib.Path(path)
        if not path.exists():
            return PathAttributes.NONEXISTENTDIRECTORY
        elif not path.is_dir():
            return PathAttributes.NOTADIRECTORY
        else:
            # this is a directory. We need to determine whether it's
            # writable, readable or accessible.
            path_stat_mode = path.stat().st_mode
            is_writeable = stat.S_ISWUSER(path_stat_mode) or stat.S_ISWGRP(path_stat_mode) or stat.S_ISWOTH(path_stat_mode)
            if is_writeable:
                return PathAttributes.WRITEABLEDIRECTORY
            else:
                is_readable = stat.S_ISRUSER(path_stat_mode) or stat.S_ISRGRP(path_stat_mode) or stat.S_ISROTH(path_stat_mode)
                if is_readable:
                    return PathAttributes.READONLYDIRECTORY
                else:
                    return PathAttributes.INACCESSIBLEDIRECTORY

This function returns the *type* of the item, using our Enum. Ignore the ``stat``
lines, since they're irrelevant to this post. If you must know, they check the
user permissions for a given path.

.. code-block:: python
    :linenos:

    def rmdir(path):
        import shutil
        import oso
        path_attributes = get_path_attributes(path)
        if oso.is_allowed("can_remove", path_attributes):
            shutil.rmtree(path)
        else:
            raise PermissionError(f"You cannot delete {path}")

This function goes ahead and tries to delete the item, checking if a user has
permissions to do so.

The one line that I'm interested in here is the one that calls
``oso.is_allowed``, which does all the heavy lifting.

This function call will search for the current polar definitions that ``oso`` has
been given, and remember, *we haven't loaded a Polar file yet,* and it then
checks if there's a ``allow`` statement definition for this check.

There is none. So irrespective of what you want to do, this function will not
let you do it if there's a ``allow`` statement definition for this check.

There is none. So irrespective of what you want to do, this function will not
let you do it. Instead, it will throw a ``PermissionError.``

Why?

Remember, *Oso is deny-by-default.* You haven't given it any polar rules, so it
will deny your request. ``is_allowed`` doesn't match with anything so it will
immediately reject your request.

Now, let's go ahead and add a polar file that we will use with this script.

.. code-block::

    allow("can_remove", path_attributes: PathAttribute) if path_attributes in
    [PathAttributes.WRITEABLEDIRECTORY];

This single line is *not* a function call. It *is nothing but a statement*.
Repeat that to yourself. It is just a statement that evaluates to ``True.``

_If_ you call ``oso.is_allowed`` with 2 arguments that match the parameters
defined here, then the function ``oso.is_allowed`` will return a ``True.`` For
*all* other scenarios, it will return ``False.``

Writing your own decorator for Click
======================================

[Click](https://click.palletsprojects.com/en/8.0.x/) is one of my favourite CLI
tools. I've built several tools using it and I've found that it makes me more
productive than when I've used argparse.
Install it using:

.. code-block:: bash

    pip install 'click>=8.0.0,<8.1'

If you were to write the above program using click:

.. code-block:: python
    :linenos:

    import click

    @click.command()
    @click.

------------------------
Where's the Server?
------------------------

An easy misconception to make is that ``oso`` needs to be used with an API. It
doesn't.  In fact, you could use ``oso`` for regular applications or scripts. If
you want to dictate whether your code can or cannot do something, go right
ahead and use ``oso.`` You could recreate ``rm`` should you want to, integrating
checks for whether a user to allowed to delete a file or not. You could also
forget about even having a ``user``, you could instead use ``oso`` to decide
whether or not a particular step happens in your code. I could see this being
used for an IoT project, decided to check if your house is too hot or too cold.
Perhaps this rule could then be used in multiple places, from turning up the
thermostat to turning on the Air Conditioner, or ordering soup online, or
getting icecream.

Honestly, the sky is the limit with this.

However, one place where authorization is definitely needed is in a web app.
That's where ``oso`` was designed to be used, despite my proclivity to use it
in hacked-up scripts.

--------------
Oso and Flask
--------------

``oso`` is a very simple way to decide what a particular user can do ``Flask``
app. However, remember that ``oso`` doesn't care how or if a user is
authenticated. You can *choose* to integrate it with a user session, but this
is not really needed.

Depending on how you use logins and user sessions, I'd recommend going through
the following three sections separately.

With a barebones Flask application
===================================

Consider the following ``app.py``

.. code-block:: python
    :linenos:

    from flask import Flask
    import oso
    from flask_oso import FlaskOso

    app = Flask(__name__)
    base_oso = oso()
    oso_extension = FlaskOso(oso=base_oso)
    base_oso.load_str("""allow("anyone","can_visit","index");""")
    flask_oso.init_app(app)

    @app.route("/")
    def index_route():
        oso_extension.authorize(actor="anyone", action="can_visit", resource="index")
        return "hello world"


    @app.route("/unvisitable")
    def unpermissable_route():
        oso_extension.authorize(actor="noone", action="can_visit", resource="this route")


Run this application with:

.. code-block:: bash
    export FLASK_APP=app.py
    flask run
    # output: * Running on http://127.0.0.1:5000/

Try using ``cURL`` to query the API.

.. code-block:: bash
    curl http://localhost:5000/

You will get the ``"hello world"`` response from this route.

Now try using ``cURL`` to query ``/unvisitable.``

.. code-block:: bash
    curl http://localhost:5000/unvisitable

You will get a ``403 Unauthorized`` from this route.

.. code-block:: html

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>403 Forbidden</title>
    <h1>Forbidden</h1>
    <p>Unauthorized</p>


Now add a new route.

.. code-block:: python
    :linenos:

    @app.route("/hello")
    def hello_route():
        return "hello again"

Rerun the app, and ``cURL`` the ``/hello`` route.

.. code-block:: bash

    curl http://localhost:5000/hello

You will get a ``"hello again"`` response. However there is no
``flask_oso.authorize`` check here.

What's going on?

While ``oso`` *denies by default*, ``flask_oso`` will have to be told to do so,
or it doesn't check for any rule whatsoever.

So, add this line at the very bottom of ``app.py`` and rerun the last ``cURL``
command.

.. code-block:: python
    flask_oso.require_authorization(app)

*Remember, there's no indentation here. This is **outside** any function or view.*

.. code:: bash

    curl http://localhost:5000/hello

Now try running this route.

Immediate you see the following ``500 Server Error`` and on inspecting the server's
output, you see the following:

.. code-block::

    Traceback (most recent call last):
    File "/home/user/oso-examples/env/lib/python3.9/site-packages/flask/app.py", line 1970, in finalize_request
        response = self.process_response(response)
    File "/home/user/oso-examples/env/lib/python3.9/site-packages/flask/app.py", line 2267, in process_response
        response = handler(response)
    File "/home/user/oso-examples/env/lib/python3.9/site-packages/flask_oso/flask_oso.py", line 225, in _require_authorization
        raise OsoError("Authorize not called.")
    polar.exceptions.OsoError: Authorize not called

``polar.exceptions.OsoError: Authorize not called`` is immediately telling us
that there is some route that hasn't explicitly run ``oso_extension.authorize``
to check for the right permissions. This is a useful setting to keep active,
but if you don't want to write some rule that looks like:

.. code-block::

    allow("anyone", "can_query", "this");

And in the route:

.. code-block::

    @app.route("/hello")
    def hello_route():
        oso_extension.authorize(actor="anyone", action="can_query", resource="this")
        return "hello again"

Which works as a sort of catch-all to allowing anyone to visit a route,
you can choose to use  the ``@flask_oso.skip_authorization`` decorator instead.

.. code-block:: python
    :linenos:
    from flask_oso import skip_authorization

    @app.route("/hello")
    @skip_authorization
    def hello_route():
        return "hello again"

.. note:: Decorator Ordering

    Any third-party decorators have to come **after** the ``flask`` decorators.

An interesting thing to note thus far is that there has been **no authentication**
of any sort in our app. Additionally, we seem to have forgone the use of
``oso.is_allowed`` and instead rely on ``flask_oso.FlaskOso().authorize.``

``flask_oso.FlaskOso()`` provides a general wrapper around ``oso.Oso``, and maps
it to the application as a ``Flask`` extension. This not only allows us to use
``oso`` as an extension, but it also allows us to have *more* than one
``flask_oso.Flask_Oso()`` object, thus enabling us to have multi-tiered
authorization should we dare to.

Additionally, ``flask_oso.Flask_Oso()``'s ``authorize`` method is a wrapper around
``oso.is_allowed``, and it allows us to explicitly name the ``actor``, the ``action``
and the ``resource.`` While *all* of ``oso``'s use case can be assumed to fall in
to these three buckets, remember again that *you do not need to follow this
paradigm*.  Understanding this enables you do do this:

.. code-block::
    allow(1, "can_be_added_to", 1);

Which can be used in Python as:

.. code-block::

    @app.route("/add")
    def check_add():
        oso_extension(actor=1, action="can_be_added_to", resource=1)
        return "1 can be added to 1, giving 2"

While this may seem like quite the trivial nonsense, I deplore readers to
spend some time thinking why or how they could use something like this.

That being said, let's get into implementing ``oso`` with a proper authenticated
session.

With Flask-Login
===================

``Flask-Login`` is a popular ``flask`` extension for creating logins. I recommend
going through its official docs to understand how to set it up.

For now, here's a barebones app.

.. code-block:: python
    :linenos:

    from flask import Flask, request, jsonify
    from flask_login import LoginManager, login_required

    app = Flask(__name__)
    login_manager = LoginManager()
    login_manager.init_app(app)

    class User:
        def __init__(self, id=None):
            self.id = id

        @staticmethod
        def get(id):
            if id == "admin":
                return User("admin")
            else:
                return None

        def is_authenticated(self):
            return self.id == "admin"

        def is_active(self):
            return self.id == "admin"

        def is_anonymous(self):
            return self.id is None

        def get_id(self):
            return self.id


    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)


    @app.route("/login", methods=["POST"])
    def login():
        username = request.get("username")
        password = request.get("password")

        if username == "admin" and password == "admin":
            user = User("admin")
            login_user(user)
            return jsonify(msg="login was a success!")


    @app.route("/secure_route")
    @login_required
    def secure_route():
        return jsonify(msg="this is a login-only route")

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return jsonify(msg="you have been logged out")

The above example doesn't use ``oso`` yet. It's a very simple, single user
API, where the username and password is ``admin.``

.. warning::
   Note that I do not recommend you do this sort of password check, or that you
   code ``admin`` ``admin`` in your your app. **Seriously**, don't blame me if you do
   this.

Run this file.

.. code-block:: bash
    export FLASK_APP=app.py
    flask run
    # output: Running on http://127.0.0.1:5000/

Login using ``cURL``

.. code-block:: bash
    curl -v --header "Content-Type: application/json" --request POST --data '{"username": "admin", "password": "admin"}' http://localhost:5000/login

.. tip::
   Use ``-v`` to see the Cookie response.

This responds something like this:

.. code-block::

    Note: Unnecessary use of -X or --request, POST is already inferred.
    *   Trying 127.0.0.1...
    * TCP_NODELAY set
    * Connected to localhost (127.0.0.1) port 5000 (#0)
    > POST /login HTTP/1.1
    > Host: localhost:5000
    > User-Agent: curl/7.58.0
    > Accept: */*
    > Content-Type: application/json
    > Content-Length: 42
    >
    * upload completely sent off: 42 out of 42 bytes
    * HTTP 1.0, assume close after body
    < HTTP/1.0 200 OK
    < Content-Type: application/json
    < Content-Length: 31
    < Set-Cookie: remember_token=admin|2e8e46e666c966125e1df57bf560a4aa129ee62f36b011cb01452b0b0369da88241bb0120288974a36358566b0458996e2afbc0de91a9196170c3bb0a4b9f42f; Expires=Mon, 07-Feb-2022 17:47:08 GMT; Path=/
    < Vary: Cookie
    < Set-Cookie: session=.eJwlzjEOwjAMQNG7ZGaIE9txehlk17boAENLJ8TdqcT2ly-9T7nnHsejLO_9jFu5b16WUkdvMpy8iTXJ7hIz5pgEZKaKme7QtAnAUKPanVYV00QzVArlPq7C8BSmtraOcP2c6xQLnSRWVVDrrABiJlw5kG2gY-_E5YKcR-x_jfpze5XvD7KsMUk.YCAnnA.SfBueBlbxoY1yxq-xwqN6fHudmQ; HttpOnly; Path=/
    < Server: Werkzeug/1.0.1 Python/3.9.1
    < Date: Sun, 07 Feb 2021 17:47:08 GMT
    <
    {"msg":"login was a success!"}
    * Closing connection 0

Copy the ``Set-Cookie: session:`` value to use in the following command:

.. code-block:: bash
    curl --cookie "session=.eJwlzjEOwjAMQNG7ZGaIE9txehlk17boAENLJ8TdqcT2ly-9T7nnHsejLO_9jFu5b16WUkdvMpy8iTXJ7hIz5pgEZKaKme7QtAnAUKPanVYV00QzVArlPq7C8BSmtraOcP2c6xQLnSRWVVDrrABiJlw5kG2gY-_E5YKcR-x_jfpze5XvD7KsMUk.YCAnnA.SfBueBlbxoY1yxq-xwqN6fHudmQ; HttpOnly; Path=/" http://localhost:5000/secure_route

.. note::

    While ``curl`` is a great tool, it might intimidate users somewhat if you're not used to a CLI. In those cases, I'd recommend using Postman, or, if you want an easier CLI, I'd also recommend [httpie](https://httpie.io/?_blank).

    For the rest of this blog article, I am going to use httpie, which helps do the same steps above through:
    .. code-block:: bash
    http http://localhost:5000/login username=admin password=admin --session test

    This stores the session cookie in a local file attached to this session name.

    .. code-block:: bash
        http http://localhost:5000/secure_route --session test

    This will then use *that* cookie effortlessly on your part.

    Note that ``http`` is how you use the ``httpie`` command. Please [check the docs to learn more.](https://httpie.io/docs)


This gives us the following response:

.. code-block:: json

    {
    "msg": "this is a login-only route"
    }

This is now a login-only route. While that solves our purpose of whether a
user is authenticated or not, this doesn't do anything related to whether a
user can access a particular route or not.

This is where ``oso`` comes in.

Modify the above file to use ``oso``:

``````python
from flask import Flask, request, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from oso import Oso

app = Flask(__name__)
app.config["SECRET_KEY"] = "this shouldn't go into the code. store it in a config."
login_manager = LoginManager()
login_manager.init_app(app)


class User:
    def __init__(self, id=None):
        self.id = id

    @staticmethod
    def get(id):
        if isinstance(id, str):
            return User(id)
        else:
            return None

    def is_authenticated(self):
        return self.id is not None

    def is_active(self):
        return self.id is not None

    def is_anonymous(self):
        return self.id is None

    def get_id(self):
        return self.id


base_oso = Oso()
base_oso.register_class(User)
base_oso.load_str("""allow(user: User, "can", "logout");""")
base_oso.load_str("""allow(user: User, "can", "logout") if user.id = "admin";""")


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    # no password check
    user = User(username)
    login_user(user, remember=True)
    return jsonify(msg="login was a success!")


@app.route("/insecure_route")
@login_required
def insecure_route():
    return jsonify(msg="anyone who's logged in can query this route.")


@app.route("/secure_route")
@login_required
def secure_route():
    username = current_user.id
    if base_oso.is_allowed(User(username), "can_access","secure_route"):
        return jsonify(msg="this is a login-only route accessible only by admin")
    else:
return "access denied", 403


@app.route("/logout")
@login_required
def logout():
    username = current_user.id
    if base_oso.is_allowed(User(username), "can", "logout"):
    # this line will allow all logged in users to be a ble to logout.  logout_user()
        logout_user()
        return jsonify(msg="you have been logged out")
    else:
        return "access denied", 403

``````

Now, this application has some Oso rules implemented in it. Let's break this down:

First, there is a ``base_oso`` object that is an instance of ``oso.Oso.`` This
is nothing special, just the ``oso.Oso`` object we've been using so far.

To this, we have called ``register_class``, which allows us to use a Python
class definition within the rules. I'll get to that in due time.

After the class definition, we are adding 2 rules by using the ``load_str``
method.

Now that we've used ``load_str`` fairly enough, let's switch to a more
convenient way, by calling ``load_file`` instead.

Change the lines:

``````python
base_oso.load_str("""allow(user: User, "can", "logout");""")
base_oso.load_str("""allow(user: User, "can", "logout") if user.id = "admin";""")
``````

To:

``````python
base_oso.load_file("policies.polar")
``````

which you should store in the same folder as your ``app.py`` file. Remember,
for any queries, please look at the [Github repository](https://github.com/stonecharioteer/blog/tree/master/code/oso-examples).

This will read the file ``policies.polar`` and load each policy written therein.

From now on, we are going to call this instead of using ``load_str.``

Next, we create an instance of the ``flask_oso.FlaskOso`` class, and pass it
the newly created ``base_oso`` object. This provides a nifty plugin with which
to use the functionality of ``oso.`` Following the standard Flask plugin designs,
this object requires you to either pass ``app`` to it during the initialization,
or to call .``init_app(app)`` afterwards (as you would with a ``create_app``
application factory function).

Now, wherever we need to access ``oso``, we need to use the newly created ``flask_oso_plugin``
object instead. This object has ``oso`` as a child, pointing to the raw layer
that Oso provides underneath.

{% capture value %}
While you wouldn't necessarily call ``flask_oso_plugin.oso.is_allowed`` in your code, I am taking a moment to explain what you'd have to do if you stuck to your guns and decided to not use the ``flask_oso`` helper functions that I will show you later. The Osohq docs do a good job of directly jumping to the best practices, but I prefer an "explicit is better than implicit" approach when it comes to explaining things that take a while for a user to understand.
{% endcapture %}

{% include note.html title="Using ``flask_oso.oso`` vs using ``flask_oso.authorize``" alert_type="info" content=value%}

Let's test the API.

``````bash
http POST http://localhost:5000/login username=admin password=admin --session test
``````

This logs us in. Let's try accessing one of the new routes.

``````bash
http http://localhost:5000/insecure_route --session test
``````

This returns:

``````
HTTP/1.0 200 OK
Content-Length: 55
Content-Type: application/json
Date: Tue, 09 Feb 2021 17:43:28 GMT
Server: Werkzeug/1.0.1 Python/3.9.1
Vary: Cookie

{
    "msg": "anyone who's logged in can query this route."
}

``````

Now, try accessing ``/secure_route``

``````bash
http http://localhost:5000/secure_route --session test
``````

This returns:

``````
Content-Length: 13
Content-Type: text/html; charset=utf-8
Date: Sun, 14 Feb 2021 07:42:27 GMT
Server: Werkzeug/1.0.1 Python/3.9.1
Vary: Cookie

access denied
``````

What happened?

In the ``/secure_route`` view, notice how the Oso policies are read and checked,
just like we have been doing so all alone.

``````python
@login_required
def secure_route():
    username = current_user.id
    if base_oso.is_allowed(User(username), "can_access", "secure_route"):
        return jsonify(msg="this is a login-only route accessible only by admin")
    else:
        return "access denied", 403
``````

Here, we call ``base_oso.is_allowed``, just like before, and check if a ``User``
object, created with the ``username`` value, is *allowed* to read this route.
While that explains what we're trying to do, remember that *all Polar is*
*looking for is:* **a line in the loaded policies that matches
``allow("admin",** **"can_access", "secure_route");``**.

Again, for emphasis, Oso only looks for a matching policy. Since we don't have
such a policy in the loaded policy file, it immediately resolves this function
call to ``False``, and our ``if`` statement moves to the ``else`` block.

Now, while this is a fine way to use Oso in a Flask app, and there's no reason
you shouldn't do this if you want to, when you have a larger Flask app, things
can get complicated. So, the Oso team has given us a Flask extension called
``flask_oso`` that helps us even more.

Let's rewrite the above file using ``flask_oso.``

<!-- TODO: rewrite the flask example above in flask_oso -->
``````python
``````

Now, query ``/secure_route.`` Notice that there's no difference in the response.
You still get a 403 because there's no policy in the ``policies.polar`` file that
allows this. However, notice that nowhere do we call ``base_oso.is_allowed.``
Instead, we use the ``flask_oso_extension`` object, which is a
``flask_oso.FlaskOso`` object, bound to the ``base_oso`` object. And therein, we
use ``flask_oso_extension.authorize`` instead. Here, the plugin does the bit
regarding the 403 itself, allowing us to focus on more important,
business-facing code.


This is a route that is decorated with both ``@login_required`` and with ``@skip_authorization.``

Let's take a closer look.

``````python
@app.route("/insecure_route")
@login_required
@skip_authorization
def insecure_route():
    return jsonify(msg="anyone who's logged in can query this route."
``````

Flask-Login's ``@login_required`` ensures that there is a session attached to
this request. If you were using cURL, you'd need to pass the cookie with the
request. ``httpie`` does this for you with ``--session <session-name>.`` Now,
notice that I've added ``@skip_authorization`` to the decorator list.

Now, we are still using ``User`` to bind the current user to an oso-accepted
object. This is a huge limitation, which the Oso crowd has solved yet again for
us.

### With ``flask_jwt_extended``

## Advanced Patterns

## Getting Help

Oso has a great support system. Their [official website](https://www.osohq.com)
is a good place to start, and you can find the
[documentation](https://docs.osohq.com) from there. I recommend looking into
their [Slack server](), which is integrated (no joke) into their website for
some great support. I reached out to [Gabe](mailto:gabe@osohq.com) through
their integrated chat, and he helped me grok Polar in a great way.

Here are some other links:

1. [Getting Started with Oso](https://docs.osohq.com/getting-started/quickstart.html)
2. [Python Oso Server Example](https://github.com/osohq/oso-python-quickstart)
3. [Flask Oso Tutorial](https://github.com/osohq/oso-flask-tutorial)
4. [Flask Oso Integration Example](https://github.com/osohq/oso-flask-integration)
5. [Oso Github Repository](https://github.com/osohq/oso)
6. [Osohq Youtube Channel](https://www.youtube.com/channel/UCrDCuHLJ32Cn0-j9K6wMwAg)
7. Youtube Talks:
   1. [Sam Scott: Access Control Patterns in Python](https://www.youtube.com/watch?v=UpPPuBqGbso)
   2. [Polar, a Declarative Policy Language](https://www.youtube.com/watch?v=fw8wRl7HbDo)
   3. [Building an Open Source Policy Engine in Rust](https://www.youtube.com/watch?v=NkatWt2_kks)

Additionally, like I've mentioned before, go through the examples in the
accompanying [Github repository](http://github.com/stonecharioteer/oso-examples)
for this post. You might want to rewind a few commits to see how the code
evolved, so that you understand the flow of the article as well.

## Cookiecutter Template

I maintain a bunch of all-encompassing Flask cookiecutter templates, and I've
added Oso to all of the templates which have auth built into them. You can find
the [cookiecutter repository here](https://github.com/stonecharioteer/cookiecutter-flask-multi),
and [the instructions on running them here](/cookiecutter-flask-multi).

## Conclusion

I don't know if there's a logical conclusion to this article. It's unlike
anything I've published before on my blog. Oso has been a sheer joy to work
with, and I'm looking forward to digging into it using Rust next. I want to
learn how to hook into the ``resource`` fields, and actually do some real damage.
It helps that the folks at Oso are super friendly.

I'd like to thank Greg for his patience. I've been running my mouth all around
HN promising them this blog article since January 2021, but truth be told, it's
been ridiculously slow and their API evolved in that time. The sections on the
``resource`` fields wouldn't have been written if I'd written this in January, so
I'll write this off as a win.

Oso is sheer joy to work with. I love their documentation, which was really
poor when I began using it, and is really well done now. I'm a strong proponent
of good documentation, which should be readable and entertaining, and their
docs fulfill that requirement.

The folks at Oso are super nice as well, so go on and trouble them on Slack.
I'm leaving yet another promise to write a long post on hooking into ``resource``
by forking Oso itself, but that's for another day. Greg, when you see this,
remind me to get to work on that :smiling_imp:.
