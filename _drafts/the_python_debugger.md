---
title: The Python Debugger - PDB or Bust
layout: post
categories: [python]
image: /assets/img/posts/pdb.png
description: "Getting to know the Python Debugger"
customexcerpt: "So you've been debugging using print? Get to know `pdb`"
---

* table-of-contents
{:toc}


When I first picked up Python, I learned to debug my programs
using `print` like everyone else. I eventually got around to
improving my game and using the `logging` module. However,
Python comes with a very good debugger. If you have been
using an IDE such as PyCharm, or an editor like VS Code that
gives you debuggers built-in, you are actually internally
using a very powerful tool called `pdb`: the Python debugger.

## Hello `pdb`
