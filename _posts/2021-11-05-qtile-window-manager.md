---
title: The Qtile Window Manager
categories: ["linux", "productivity", "preferences"]
layout: post
---

I've been an avid user of XFCE for a very long time. I'm fond of its
lightweight nature, and I feel productive in it.  But when I first discovered
tiling window managers, I was mind-blown. I've wanted to use one forever.

My first experience with one was a few years ago, before I understood how Linux
window managers worked. I couldn't yet wrap my head around the fact that you
could install more than one window manager and choose what you wanted during
login. I think I've grown since then. I faintly remember trying to install
[i3wm](), the most famous tiling window manager at the time. I think I was taken
aback by the black screen, and more so with the mouse pointer which just said
`X`.

A year or so ago, I came across [DistroTube's Youtube Channel](), where he
talks about [xmonad](), the tiling window manager that's written in Haskell.
While I've been wanting to learn Haskell for a very long time, my career
trajectory hasn't afforded me the chance to learn it so far.

I've since moved jobs and completely shifted to Linux everywhere. I no longer
want to use a non-linux machine ever again. I'm sure there's a whole blog
article about how much of a Linux person I've become in the past year or so,
somewhere in me.

Last week, I came across [dt's video on Qtile](), the [tiling window manager
written entirely in Python](). Now *that* was truly enticing. I'm adept enough
in Python to be able to manage complex configurations all on my own. And after
skimming through the documentation, I spent a day modularizing the [default
qtile config]() since the default config gives me goosebumps, and not in a good
way.

In this article, I'll describe what I did, and how I went about it.

## Configuring Qtile

I decided to abstract away the entire configuration so that it doesn't live in
my [dotfiles]() repository. I wanted to create a python library for myself so
that it would have a bunch of utilities for my own consumption. This is where
the [stonecharioteer](https://github.com/stonecharioteer/pystonecharioteer)
repository comes in.

Additionally, I disagreed with the default way of installing Qtile. As a
principle, I *never* `sudo pip install` *anything*. Instead, I asked my friend
[Karthikeyan Singaravel](), who is a Python core developer, and he recommended
using the [deadsnakes PPA for Ubuntu]() to install any version of Python that I
chose. I tried compiling python 3.10 myself, installing to `/opt/qtile/` using
`configure --prefix /opt/qtile/` during the configuration stage of the source
code. However, I admit that using `deadsnakes` is a far better idea since I
could create a virtual environment based on `python3.10` into `/opt/qtile/`
instead. I had to change the owner of the folder to my user account. Note that
I *could* store the virtual environment in my home folder and just use that,
but I wanted to isolate this *outside* of my home folder.

So, I installed `python3.10-full` and `python3.10-dev` (the development header
files are necessary for building some of the dependencies of `qtile`), and I
created a virtual environment using the `venv` module in `/opt/qtile`. Then, I
changed the owner of the folder to my regular user account.

Then, it was time to install qtile.

Since I use the [fish shell](), I had to `source activate /opt/qtile/bin/activate.fish` to activate the virtual environment. And then I followed up by installing `qtile`. I didn't pick a version right away, I decided to go with the latest version.

Qtile doesn't setup an entry for your `xsessions`, so you need to do that yourself. 

I created `/usr/share/xsessions/qtile.desktop` and filled it with the following:

```ini
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Exec=/opt/qtile/bin/qtile start
Type=Application
Keywords=wm;tiling
```

Notice how I used the *absolute* path for qtile.

After this, I logged out of my previous window manager and switched to the new entry for Qtile.

On loading qtile for the first time, I was fairly surprised with the default config. It wasn't as *blank* as i3wm and xmonad were. It had a panel, a helpful text field on the panel about how to start the launcher, and it was very easy to use. I was liking it already.

But I wanted to configure it so that I could mess with the design.

![Default Config](assets/images/posts/qtile/default.png)
*Fig. 1. Default Qtile Config*

The first thing that bothered me was the lack of a wallpaper. I'd used [nitrogen]() before, so I installed it and started it up, setting a wallpaper. I restarted qtile and then... nothing.

That was me being silly and forgetting that *Explicit is better than Implicit*. Like all tiling window managers, Qtile did none of the work for us. You have to ensure that the wallpaper manager *loads* when Qtile is done loading. That's where the `.xsessionrc` file comes in.

Since nitrogen can restore a wallpaper with ease, all I needed to do was:

```
nitrogen --restore &
```

This went into the `~/.xsessionrc` file.

Next, I needed to start configuring Qtile.

Qtile's config file rests at `~/.config/qtile/config.py`. On start, Qtile will *read* this file. Since this file is just Python code, that also means every single line in this file is executed.

When you look at the
[default config](https://github.com/qtile/qtile/blob/master/libqtile/resources/default_config.py),
you will notice:

1. It's about 130 lines long. Not too big.
2. It's just a bunch of variable declarations.

This meant that all you needed to configure Qtile was to ensure you set the
values of a few *global* variables in the config file. And Qtile would take
care of the rest.

This was useful. All I needed to do was set some variables.

The default config constructs all these variables as it sets them, which is
something I don't recommend. Python's error handling will not point out the
right place where the error is occurring, and while 3.11 seeks to improve this,
it's generally not a good practice to have a long variable declaration step in
your code.

For example, where the config does this:

```python
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
]
```

If you want to *reuse* these objects, it's better to just construct them separately and then use them in a panel. The same goes for reusing panels.

So instead, I decided to create a python library to manage, among other things, my qtile configuration.

This library needed to serve other purposes, and it was always going to be very esoteric. I wanted to be able to use it to create a CLI for some helper tasks, and to store my ansible playbooks as well.

For now though, I'm just going to store my qtile configuration builder.

### Poetry

I've been a staunch supporter of using `setuptools` to create python packages.
I've never used [poetry](https://python-poetry.org/), and I thought perhaps now
is a good time to move away from a `setup.py` and start using a
`pyproject.toml`. With that in mind, I installed poetry following the
instructions on the website. Note that while the large block in the center
tells you to use one command, there's a callout above it that also tells
you that the `get-poetry.py` script is about to be deprecated.

To install poetry, run:

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

Poetry is a python packaging and dependency management system. You setup a new project using it, and you can manage the virtual environments, manage dependencies, isolate primary dependencies, manage developer dependencies, and more with it. I've begun moving away from `miniconda` and have taken a liking to deadsnakes, but I might just start using poetry for everything. The requirements.txt file is frankly annoying to maintain.

I created a new project using:

```
poetry new stonecharioteer
```

This created a placeholder repository for me, which had a `pyproject.toml` file, a tests folder, a module folder, named `stonecharioteer`.

```
stonecharioteer/
├── poetry.lock
├── pyproject.toml
├── README.rst
├── stonecharioteer
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_stonecharioteer.py
```

There are [some](https://realpython.com/effective-python-environment/#poetry)
[great](https://python-poetry.org/docs/) tutorials for learning how to use poetry, so I'm not going to go into it here. What I found the most useful are the following commands:

```bash
# create a new project
poetry new stonecharioteer
# add a dependency for the project
poetry add requests
# add a development dependency for the project
poetry add --dev pytest
# install updates to the dependencies
poetry update
# launch a shell with a virtual environment sourced for this project.
poetry shell
# create a new environment with a different flavour of python
poetry env new python3.10
# build the wheel
poetry build
# publish to pypi
poetry publish
# bump the patch version
poetry version patch
# bump the minor version
poetry version minor
# bump the major version
poetry version major
```

### Modularizing the Qtile Config

As I've written above, the `config.py` file needs to merely contain the following variables:

1. `keys`: These are the keymaps for Qtile.
2. `screens`: These are physical display spaces your computer might have, like monitors.
3. `mouse`: These are mouse behaviours.
4. `groups`: These are synonymous with workspaces, and define the names of various workspaces.
5. `layouts`: These are the tiling window manager layouts you'd like to enable.
6. `terminal`: This points to your preferred terminal. You should add the terminal to path if you'd like to use it.
7. `mod`: This is the modifier key, usually set to the Super or Windows key.

There are a few *other* variables that you can set, but I don't think they're necessary always. The defaults will persist.
## Rice Screenshots

![Home Screen](assets/images/posts/qtile/rice-001.png)
*Fig 1. Home Screen*

![Terminals](assets/images/posts/qtile/rice-002.png)
*Fig 2. Multiple Open Terminals*

![Browser](assets/images/posts/qtile/rice-003.png)
*Fig 3. Browsers*

## Todo

This project isn't done yet. I have a list of things I want to do, some of
which are:

1. Create Ansible playbooks for the installation.
2. Create a linux user group for the virtual environment. and add all relevant
   users to it.
3. Create icon-based widgets for the panels:
    1. Create a widget to tell me when the latest chapter of One Piece is out.
    2. Create a gmail widget that filters and only tells me about mails I'm
      interested in.
    3. Create a widget for tmux sessions
    4. Create a battery indicator
    5. Create a CPU usage indicator
    6. Create a nordvpn indicator
    7. Create a widget to monitor storage space on the NAS.
    8. Create a widget to list the current kubernetes context.
4. Update the `screens.py` file to adaptively add panels when it detects multiple monitors. Allow users to control the monitors using a configuration file.
5. Add hooks to bind windows to certain screens (workspaces).
