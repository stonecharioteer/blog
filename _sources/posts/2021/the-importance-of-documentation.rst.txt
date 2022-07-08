:blogpost: true
:date: April 28, 2021
:category: Tech
:tags: [documentation, teaching, writing]

.. _documentation-1:

================================
The Importance of Documentation
================================

Nod if you've come across this before. You find an *amazing* software library
that you can use for your project, whether at work or one of your many
side-projects, and you find the documentation just *lacking*.

I've been here, and I'm certain you have as well.

My first job began with me writing what is called a Standard Operating
Procedure or ``SOP`` document. In other circles, this is called a Work
Instruction, or a Run Book. This was *not* a fun exercise. I naively believed
that as long as I wrote it well, I was doing a good job.

I was wrong.

The users found it hard to read. While I'd succeeded in capturing the process in
readable, concise English, I'd made the mistake of assuming that the person
reading the document would be like me.

Somehow, I've always been a believer of "well-written documentation". I am not
so certain that the quality of the writing matters as much as the way it has
been written though. I'm certain you don't want docs that read like a Charlotte
Bronte novel, for all that you enjoyed reading *Jane Eyre*.  Every piece of
documentation needs to stay cognizant of *who* is going to read it.

This is hard though.

When you write a ``README.md`` in your Git repository, *who* is going to read
it?

When you write a blog post in your company's tech blog, *who* is going to read
it?

When you write a conference talk submission, *who* is going to read it?

When you write the API section of your documentation, *who* is going to read
it?

When you write a ``Getting Started`` guide, *who* is going to read it?

When you write an Invention Submission document for the Legal and Invention
Protection department in your organization because you'd like to file for a
patent, *who* is going to read it?

If you're not asking yourselves these questions, and if you're constantly
writing your documentation as though the *same* sort of people are going to
read all these sections, then you might as well stop writing the document in
the first place.

Consider the ``README.md`` file. Someone who arrives at this file comes to it in
one of three ways:

1. They found the repository on Google, when they were searching for something.
2. They found the repository when they were searching for keywords in Github
   (or on Gitlab, or your company's installation of whatever SCM they picked)
3. They found the repository linked in some tech blog post
4. They found the repository linked in some tech-centric social media post.

There's a pattern here. The people who find your repository this way are
*cutting to the chase*. They're developers, or tech-savvy folk.  So don't go
into lengthy explanations of what your product is. *Show them right away!*

If you have a CLI, *mention* that. If you have a User Interface (whether a TUI
or a GUI), use *screenshots* or a GIF.  If you have a libray, show how it can
be used, maybe in a tiny code snippet that shows life both *with* and *without*
your library. If you have something that integrates a plugin system, show them
how to get plugins.

But most importantly, if you have a website with more detailed docs (and you
should!), point them to it.

The audience here, is someone who can get started with your code with just this
file.  Give them the same credit you give yourself. This is someone who wants
to figure out how your tool/code works with your source code.

Here are some things to remember when you are doing this.

1. This might be a co-worker. So if you're going to need to point them to
   relevant setup instructions that may or may not involve package managers.
   (They may love installing from source!)
2. This might be someone who found a *bug* in your code and would like to
   report it. Point them to your issue tracker / relevant contact details.
3. This might also be someone who is evaluating your library for use in his
   organization. Large orgs like to see the license. Make sure you use short
   license descriptors. If you use an image though, *make* sure you also
   provide the License file in full writing in your repository.

However, a README file is not the same as a Getting Started Guide, for example.

In a Getting Started Guide, you need to ensure you talk about the following.

1. How do you install your code in the most-relevant fashion?
2. How do you check whether the code has installed (usually by checking the
   installed version)?
3. How do you get started with a small, but common use-case?
4. How do you do 2 or 3 other common activities with this code?
5. How do you find in-depth resources for each of these activities?
6. How do you find the developer manual?
7. How do you report bugs?

Some of these are the same as the ones in the ``README.md`` section, but the way
you write this will change. Now, your user may not even be a developer. They're
going to be your *user*, the person for whom you wrote this tool or library in
the first place. How do you ensure they have the least friction in getting
started? How do they get a quick taste of what your code can *do*?

That's what the Getting Started guide does. No where here do you talk about
*what* your library or tool does. That was the introduction, which the current
reader doesn't care about. Instead, they want to know how to get started.

Remember that this tonal shift keeps happening constantly. Every single page of
your documentation should feed off this belief.

*Your Getting Started Guide is not your ``README.md`` file.*

One of my favourite resources on writing documentation is `Divio's Documentation
System. <https://documentation.divio.com/>`_ There's also a `great talk that was
delivered at PyCon Australia 2017 on the topic.
<https://www.youtube.com/watch?v=t4vKPhjcMZg&feature=youtu.be>`_

While those are great resources, I'm starting a series of blog-posts on writing
different parts of your documentation, and I'll update them over the next few
weeks.

I'd like to expand on my idea of what goes into a ``README.md`` first, and then
tackle how to write the other parts of documentation in dedicated posts.

---------
Series
---------

1. :ref:`How to Write Documentation: The README.md file <documentation-2>`
2. How to Write Documentation: The Getting Started Section
3. How to Write Documentation: The Installation Guide
4. How to Write Documentation: The API Reference
5. How to Write Documentation: Conference Talk Submission
6. How to Write Documentation: The Tech Blog
7. How to Write Documentation: Patent Submission Document
8. How to Write Documentation Extras: The Uninstallation Guide
9. How to Write Documentation Extras: The Configuration Guide
10. How to Write Documentation Extras: Testing Instructions
11. How to Write Documentation Extras: The Changelog
12. How to Write Documentation Extras: The Roadmap
13. How to Write Documentation Extras: Issue Tracking
14. How to Write Documentation Extras: Presentations
