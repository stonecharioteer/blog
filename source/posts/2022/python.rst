:blogpost: true
:date: Jan 7, 2022
:category: Tech
:tags: Python, Developer Experience, Development Environment

=================================
Python - A Reflection in 2022
=================================

I built my career on Python. In 2014, I had to make a decision. It was between
either choosing to learn Ruby or Python. I was helping to create a tool and
process for a team of content writers at Flipkart -- I was a content writer
there, and I'd used Excel for it at first, until Excel couldn't handle the
queries anymore. I called my friend who recommended Python. I learnt Python,
almost over a course of a weekend, and I was making a PyQT4 application in a few
weeks.

.. note::

   Before you read this post, it might be prudent to read
   :ref:`for-those-who-came-in-late`

I knew nothing about software development. I was using Github to store the code,
this was a personal project. And I was having fun. It was enjoyable, really. The
I installed Python on all my colleagues' laptops, and my application ran. I
eventually found PyInstaller and gave them all executables instead. It was
really fun.

Somehow, I wonder if the entrypoint to Python has changed in the years since.
I still like the language -- it's still my primary source of income. However,
something about it seems to have changed at a fundamental level.

I didn't learn about virtual environments until a long time later. I was using
Python 2.7, since I learnt from Zed Shaw, who was a staunch opposer of Python 3
for the longest time. I didn't need any of that.

Today, if someone came to me and asked me about getting started with Python,
what would I tell them? Would it be the same things I experienced, or would I
overwhelm them with unnecessary tooling?

What's the best way to install Python on your machine? I no longer run ``sudo
apt-get install python python-pip``. I don't remember the last time I had to use
`get-pip.py. <https://github.com/pypa/get-pip#get-pippy>`_ I have used
`miniconda, <https://docs.conda.io/en/latest/miniconda.html>`_ `Anaconda,
<https://www.anaconda.com/>`_ `asdf, <https://asdf-vm.com>`_
`pyenv, <https://github.com/pyenv/pyenv>`_ and `poetry. <https://python-poetry.org/>`_
Right now, I like ``asdf``, but I have a feeling I won't use it too long. That
deserves a post in and of itself really.

What's the best way to manage dependencies? Is it creating a
`virtual environment <https://docs.python.org/3/tutorial/venv.html>`_
and capturing the dependencies in a ``requirements.txt`` file, or perhaps you'd
like to use ``poetry`` to do that and store only your direct dependencies in a
`pyproject.toml <https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/>`_ file?
Maybe you've heard of `pip-tools <https://github.com/jazzband/pip-tools>`_ and
want to use a ``requirements.in`` file which you can then use to generate a
``requirements.txt``. Or do you want to write the requirements file yourself?
Have you heard how `nodejs, <https://docs.npmjs.com/cli/v7/configuring-npm/package-lock-json/>`_
`Rust <https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html>`_ and
other languages generate a ``.lock`` file or with the hashes of the dependencies
so you're safer when using other registries? Maybe someone has told you you
should be looking at the output from `dependabot <https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/>`_
when you get an alert about malicious packages or packages with
vulnerabilities.

And deployment. How do you deploy? Do you recreate your development environment
in a cloud server? Perhaps you have a nice little shell script that does this.
Or maybe you've heard of `Ansible, <https://www.ansible.com/>`_ to automate
this. Or maybe `Packer. <https://www.packer.io/>`_ Or maybe your company has its
own deployment tool. Do you use `Docker <https://www.docker.com/>`_ or
`Kubernetes? <https://kubernetes.io/>`_ Do you still use Docker or should you
use `Podman? <https://podman.io/>`_ And how do you build a Docker image anyway?
Should you redo the steps you're doing on your laptop on your container or
should you just use a version-tagged python container and then install packages
at a global level because the container runs in an isolated environment, using
something you've heard called `cgroups? <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/ch01>`_

Isn't this *exhausting?* I find it to be. It wasn't this way before. And I've
still not spoken about `Typing <https://docs.python.org/3/library/typing.html>`_
and uploading your `.tar.gz <https://stackoverflow.com/questions/45168408/creating-tar-gz-in-dist-folder-with-python-setup-py-install>`_
or `wheel <https://realpython.com/python-wheels/>`_ file to `pypi.org.
<https://pypi.org/>`_ And I've not spoken about Python versions yet.

What's even going on in the Python world? Somehow, the language is becoming less
enjoyable to me. I remember having so much fun with it. What happened to the Zen
of Python.

  There should be one-- and preferably only one --obvious way to do it.

What happened to that? As it stands, these are only the ways I remember off the
top of my head. I haven't spoken about `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_
or `pipenv <https://pipenv.pypa.io/en/latest/>`_ or
`the deadsnakes PPA for Ubuntu. <https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa>`_
The role of all these tools is to make things easier, so why does it feel so
*tiresome?* I cannot imagine how it must feel as a newcomer to
this world. Do bootcamps cover all this? They'd lose me on day 1. I have been in
the business of mentoring younger developers and students who reach out to me
for help, and I never really tell them all this stuff. It seems tiresome *to
me*, and I cannot imagine what they must feel.

In the last few weeks I've been learning Golang and I admit, I've had the
longest resistance to Golang. I wanted to, *want* to, learn Rust instead, but
Go is more popular, and it's easier to convince people to pick it up as opposed
to getting them excited about Rust. I still want to learn Rust and build things
with it, but I want to use Golang for whatever I've been doing with Python.

`gopls <https://go.googlesource.com/tools/+/refs/heads/master/gopls/README.md>`_
has been a sheer joy to use with Neovim, and I've never had that sort of
experience with Python, even though I use `pyright. <https://github.com/Microsoft/pyright>`_

But I still love Python. It's been my main language for about 8 years now. I
didn't know any other language enough to build things with before it. And I had
*fun* with it. I cannot imagine even building half the things I've built with
Python in any other language. But I feel like I want to return to the basics
with it.

What does that entail? I'm not sure really. I've tried downloading and building
versions of Python and using ``python3 -m venv env`` to create environments,
but it feels too clunky a process. Or perhaps, whenever I need a new
environment, I can build an entirely new version of Python, store them all in
``~/python/py<version>/<project-name>``, and use `direnv <https://direnv.net/>`_
to automatically enable/disable it when I enter the folder.

.. tip::

   Did you know about `shims? <https://en.wikipedia.org/wiki/Shim_(computing)>`_
   I had been searching for something like this for ages and didn't know what
   the right term was! Direnv is *amazing*.

The state of Python both excites and exhausts me. It's good that there are so
many tools now, but it cannot be easy. If I delve on this too much, I might end
up making my own tool. It'll end up being like the battle of the Frameworks. And
for what it's worth, I still think Flask is better than Django. I'm more attuned
to doing things explicitly than having an entire framework do things for you.
Call me old fashioned.
