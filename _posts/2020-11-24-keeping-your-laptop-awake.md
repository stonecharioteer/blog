---
blogpost: true
date: Nov 24, 2020
category: Tips and Tricks
tags: wfh, linux, python
---
# Keeping Your Work Laptop Awake

Sometimes you'd like to keep your work laptop from sleeping, and for whatever
reason, you might not be able to change your system's power management rules.
In this article, I show you how to get around that.

## Pre-existing Tools

Before you try this, note that there are other tools that you can use to do
this. `caffeinate` is one of them, and it should be pre-installed on your Mac
or Linux machine. I always recommend checking your power management to prevent
this, as well.

## The `keyboard` Python module

Before you do this, you should do one of two things:

1. Create a Python 3.6+ Virtual environment; or
2. Create a Python 3.6+ Conda environment.

```
python3 -m venv ~/.keyboardenv
~/.keyboardenv/bin/python -m pip install keyboard
```

*Or*:

```
conda create -n keyboard python=3.6
conda activate keyboard
pip install keyboard
```

Now, create this script and save it in your home folder.


```python
import keyboard
keyboard.press_and_release("f14")

```

Save this as `.keep_awake.py`.

Now, in your `~/.profile` file, add the following:

```
# if you are using the virtualenv method:

alias keep_awake='watch -n 300 "$HOME/.keyboardenv/bin.python $HOME/.keep_awake.py"'

# if you're using the conda method:

alias keep_awake='watch -n 300 "$HOME/miniconda3/conda/envs/keyboard/bin/python $HOME/.keep_awake.py"'

```

Note that the location of the environment will depend on where you installed
Miniconda/Anaconda on your laptop. I usually install it into the `$HOME`
directory.

Now, ensure that your directory is *sourced* in your shell's *rc* file.

Add `source ~/.profile` to the end of your `.bashrc` or `.zshrc` or the *rc*
file of your chosen shell.

## Final Notes

The `keyboard` module can be used to do a lot of interesting things, such
as making shortcuts and adding hotkeys for altered behaviour. Do explore more
and `@` me on Twitter if you build something amazing.

