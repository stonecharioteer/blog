:blogpost: true
:date: Jul 20, 2022
:category: Tech
:tags:

.. _on-building:

=====================
On Building
=====================

Have you ever built *things*? Stuff that you use more than once? Stuff that
others have used? This is a post about that process.

I love to build things. It somehow stems from my past as a mechanical engineer,
short-lived as that may have been. Crafting tools is an art, and somehow it
feels like that's the only part of this job that remains so, if you can excuse
the bleak tone.

Software Engineering is about building. I don't know about you but I came into
this field because I was having fun making tools for other people. I wanted to
reflect about that, especially since I've been writing some tools at Merkle
Science and wanted to reflect on it.

---------------------------------
Why Do We Build?
---------------------------------

Because we are humans.

Human Beings have been building tools for as long as we have existed. It's one
of the most important things about us. We are what we are as a civilization
*because* of it.

So let me ask that question in another way, *Why do Software Engineers build
things?*

Those with a business vein will tell you that it's to save costs and to make
things efficient. That's good for them, but that's an *after*-effect of building
tools. I personally build tools because the process of building them is
rewarding in and of its own. It's almost like coding ASMR, I build a tool that
I know will save me time, no matter how little, and I derive pleasure from using
that tool. One such tool is `jerry, <https://github.com/stonecharioteer/jerry>`_
which is something I use all the time in my tiling window manager.

However, tools I build for others give me greater satisfaction. One of the tools
I have built at Merkle Science is to automate our data-operations, something
that can help the data engineering team to copy data between otherwise
directly-incompatible cloud databases (the specifics aren't important to this
post). I originally wanted to build a fancy CLI for this, with all the bells and
whistles, but the team was doing a lot of data migration and fresh database
installs, so we needed something quick and dirty. So, Bash came to the rescue.

I think I've written more bash scripts after my :ref:`Bipolar Disorder Diagnosis
<bipolar-1>` than I have before. I think I'm more accepting of the fact that the
tools we build don't need to be perfect.

I digress. The main reason I've built tools is because when I'm handed a manual
task, irrespective of how small, I want to automate it. I'm a lazy developer. I
don't like doing manual tasks. My brain runs ``%s/manual/menial/g`` most of the
time.

--------------------------------------
