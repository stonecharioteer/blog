---
title: How to Write Documentation - The README.md File
layout: post
categories: [documentation, writing, meta, side-projects]
description: "A guide on how to write a README.md file for a Git repository."
---

In the introduction post to this series, I discussed how to write a `README.md`
file in a `git` repository. I'm digging deeper into this here.

Remember the perennial question when you write docs: "Who is your audience?"

With a Readme file, that person can safely be assumed to be tech-savvy.

So, to satiate their thirst, you need to cut to the chase as well. Your
`README.md` file should seek to inform instantly. It shouldn't be too long,
because the user might be reading this on Github's mobile site, or, god-forbid,
something with a horrible UI. So instead of lengthy descriptions of what your
project does, what *should* you describe?

## The Project Name

Use your project's title as the top-most heading. That gives your project more
visibility, it shows what your project *is*. While this doesn't seem like much,
remember that sometimes there are repositories which are attached to an
organization.

For example, consider a software project called, hypothetically, Sprint. Sprint
has 4 components:

1. A webservice written in Rust (`sprint/server`)
2. A Docs site written using Hugo (`sprint/docs`)
3. A CLI written in golang (`sprint/cli`)
4. A Python Library (`sprint/py-sprint`)

The names of these repositories are indicated in parentheses. While the
repository names do indicate the purpose of these repositories, do not always
assume someone who *fumbles* on your repository knows that this is attached to
a larger project.

So declare that at the *very top*. Use a project name title, just `server`
won't make sense. Instead, use `Sprint Web Service`. Remember that your
repository name doesn't have to be your project's name. Different people use
repository names for different purposes.

## The CICD Stickers

I'm not a big proponent of the pipeline stickers. If you need your pipeline to
alert you that there's something wrong, then your docs aren't the place to do
that. Do not pollute your `README.md` file with a dozen stickers. However, do
use it to indicate helpful stuff. however, you can make do *without* the
stickers, that's better.

## A Note

Add a note on who this is for. That greatly helps people perusing your README.
Especially if you have an actual developer and contributor guide somewhere.

## A Link to the Documentation

Add a link to your complete documentation website. Add a note stating that
that's where the user manual and other errata are.

## Installation Guide

Add a *very* short installation guide, albeit from source. Do not list out the
5000 package managers that you support in your tool. Those belong in your docs,
in a way that can perhaps detect the platform that your user is hailing from
and show just that.

The build steps should be as platform agnostic as can be, *or* you should
target your most likely platform. If you're building a Windows tool, don't
bother explaining how this works in Linux. If you have multiple platforms, link
instead to the online installation guide.

Link to the relevant section of your documentation where you detail other
installation methods. At this point, give your reader some credit and assume
that the note above is good enough to serve as a warning showcasing who this
docs is for.

However, remember that even with the best of warnings, you are going to have
people who come here and think that these docs are for them.

## Building the Documentation

This is an optional step, but it is necessary if building local docs is
something someone who wants to use your tool should do. However, this can also
go into your developer documentation.

## Screenshots / Recordings

*If* you are building a User Interface, be it a TUI, GUI or CLI, you need to
show what the interface looks like in a screenshot. You do not need to add a
complete gallery here, but you should add a clear picture to help users
understand what they're in for. Additionally, make sure you add a timestamp or
a version watermark to your screenshot, so when users see that something is
very different in their installation, they can immediately note that the
screenshot is from a different version. Note that if you can, you should always
update the screenshot whenever something major changes.

## License

Add a relevant, short licence note on this readme to help people understand
what license the project is using. Do not replicate the entire license here,
instead link to the relevant file. If your license has changed over time, note
the version from which the version has changed as well.

## Contributing

In the Contributing section, link to the issue tracker, and to the Developer
guide if you have one. If you don't have one, think about how many developers
are contributing to your project, and make the judgement to add a lengthier
section right here if you need it.

If you're not going to maintain a separate section, then make sure you show users
how to run tests in this section. Treat it like a mini-Developer's guide.

## Other Notes

Some other notes you can put in your README are:

1. The latest release notes.
2. A link to your Slack or Discord channel where devs can be reacted directly. I'd recommend having private channels for contributors and one public help channel that's moderated by a bot.
3. A link to your company's website, if this is a company's open source project.

## What does not belong in your README

1. Authors and Contributors list.
2. Changelog
3. The Getting Started Guide
4. Links to presentations.
5. Links to Conference videos
6. Description of your company
7. API Documentation

There *are* usecases for each of these, but they don't belong in the README. Instead, make a project website with dedicated sections for the,.

## Final Note

I'm going to be re-stating this time and again. While you have the best of intentions, you will not be able to make everyone happy. However, that doesn't mean you shouldn't at least consider *who* your documentation is for. Make sure that you know this. That way, you will at least help some of the audience instead of triggering everyone.

## Exceptions - `httpie`

[`httpie`](https://github.com/httpie/httpie) goes against many of the points I've listed above, but it does so with an important note at the top. It *tells* the reader that this *is* a development version of the official docs which are best viewed on the docs website.

It provides a `GIF` right at the top, showing users what this tool can do. You are *sold* at the very beginning.

While the entire README actually is their documentation, they do it in a way that showcases different aspects of this tool effectively. The `README.md` does what it's supposed to do: introduce the tool, and gives users help whenever they need it. Right at the top, the stickers are used to grand effect: to link to Discord where users can get help.

## Series

1. **How to Write Documentation: The README.md file**
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
