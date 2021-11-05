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

## Rice Screenshots

![Home Screen](assets/images/posts/qtile/rice-001.png)
*Fig 1. Home Screen*

![Terminals](assets/images/posts/qtile/rice-002.png)
*Fig 2. Multiple Open Terminals*

![Browser](assets/images/posts/qtile/rice-003.png)
*Fig 3. Browsers*

## Todo

This project isn't done yet. I have a list of things I want to do, some of which are:

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
