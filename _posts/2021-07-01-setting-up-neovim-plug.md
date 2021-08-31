---
title: Setting up Neovim with Vim Plug and YouCompleteMe
layout: post
categories: [vim]
description: "In which I describe my shift away from VSCode and how to setup nvim."
---

I'm moving to neovim for my primary editing purposes. VSCode has served me
well, but I'm growing wearing of its growing pains. Some extensions don't work
well, and many things seem broken of late. Besides, I don't really use the IDE
features all that much.

I've been using neovim for quite some time, and I like it. I grok the vim
movement keys, and I love the modes. Vim in and of itself seems to have
problems that I didn't delve into.

I don't like using others' configs. I've tried doing that, and that really
didn't work for me. I am also very pedantic about messing with global python
installations, since some of the plugins usually recommend installing
packages willy-nilly in the global python install.

## Installing Neovim

I've downloaded the latest development version of neovim from the website.

```bash
sudo mv ~/Downloads/nvim.AppImage /usr/bin/nvim
```

## Configuration

My dotfiles, as always, are 
[here](https://github.com/stonecharioteer.com/jarl).
The README.md documents everything therein, but I'm taking the time here to
talk about a particular problem I had personally when setting up YouCompleteMe.

## Installing Vim Plug

I use [vim-plug](https://github.com/junegunn/vim-plug) as my package manager of
choice.

```bash
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

The Plugins I've chosen are listed in the README of the github repository.

## Installing YouCompleteMe

These instructions are valid for Manjaro Linux running the 5.13.0-AMD-znver2
kernel, however they shouldn't vary for any version of Linux.

While most tutorials instruct you to install YouCompleteMe using the system
installation of Python, *do* **not** ***do*** that. Instead, create a virtual
environment or a *conda* environment. In fact, you'll see exactly why I
recommend using a conda environment.

```bash
conda create -n nvim python=3.9
conda activate nvim
pip install pynvim neovim
```

After creating this environment, edit the `init.vim` file and ensure that you
change the path to reflect where the `python` command in your new environment
resides.

You can check that by typing `which python` while you have the environment
activated.

```vim
let g:python3_host_prog = '/home/stonecharioteer/code/tools/miniconda3/envs/nvim/bin/python3'
```

This tells your neovim installation where to expect the python3 installation.

Make sure you activate your Vim Plug hook *after* setting this value.

After you run `:PlugInstall`, exit nvim and navigate to the `~/.local/share/nvim/plugged/YouCompleteMe` folder.

Here, with your python3 environment activated, run `python3 install.py --all`.

Then, you should start nvim to *check* if YouCompleteMe reports any errors.
You can check the STDERR logs using `:YcmToggleLogs` and then pressing `2`.

You will notice that there is a problem with `GLIBCXX_3.4.29`, which YCM reports
is missing from the `libstdc++.so.6` file in your Conda environment's `lib`
folder.

This is very easily remediable.

All you need to is delete the file that exists in your lib folder, and instead
symlink the system's `libstdc++.so.6` file into this folder. This file is usually
in `/usr/lib64`.

Ensure you have the latest `glibc` package installed on your machine.

## Note

This post is rather esoteric for a problem that I've faced just now. I thought
I'd document it because I'm prone to forget how I fixed this.

