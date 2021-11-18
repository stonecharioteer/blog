---
blogpost: true
date: Nov 30, 2020
category: Show and Tell
tags: discord, python, til, meta
image: 0
---
# Sarathi - A Personal Discord Bot

I've been maintaining [a TIL page](https://stonecharioteer.com/til.html) for a while now, and while the idea is great, I have had some issues updating the sheet daily.

![sarathi-bot add factoid](/assets/images/posts/sarathi/help.jpeg)

My flow has been like this:

1. Whenever I find a link / factoid interesting, I save them in a WhatsApp group where I'm the only member for later record.
2. I add these to the TIL page whenever I could. Lately, I've not been able to do so.

As you can see, the problems with this approach are many:

1. This is too manual. I'm someone who automates everything. I can't be doing this.
2. Finding links is hard unless I'm using `ripgrep` on a non-mobile device.
3. Categorizing things and updating the look of my TIL page is hard.

And I've been meaning to leverage a Telegram bot for this task for quite some time.

However, I have not gotten back to the task in ages, necessitating the use of my rudimentary manual method for months on end.
So this weekend, as I prep myself to shift my body clock to attend [David Beazley's RAFT Course](http://dabeaz.com/raft.html),
I decided to use the midnight oil to write my own bot, one that I could add to.

## Why Discord?

I've been using discord to talk to a few friends and communities lately, and I've found it's integration with Linux to be amazing.
I love the web-UI, and the desktop app which works quite well everywhere. I also use the mobile app on my phone and tablet.

And [it has a Python library], with quite a robust API no less.

## Resources

I relied on the following resources for this task.

1. [Real Python tutorial on creating a Discord bot](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python)
2. [Discord Official Documentation](https://discord.com/developers/docs/intro)
3. [`discord.py` documentation (quite unsatisfactory docs IMO)](https://discordpy.readthedocs.io/en/latest/index.html)

## Goals

I wanted to be able to do the following:

1. Create bot that would take arbitrary commands and parses them for a URL or factoid.
2. Extract a title from the URL if need be.
3. Maintain a time-based `json` on my Blog's github repository with all the links and factoids neatly arranged.
4. Automatically commit the `json` to github.
5. Regenerate the `til.md` file using a `jinja2` template automatically.
6. Pushing code to Github so that the blog is update instantly.
7. Allow querying of the knowledge-base with a simple search API.

## Outcome

While I won't go to much lengths to describe how I coded this bot, the Real Python article manages to do that better, I'll just go ahead and show off the result:

### Help

![sarathi-bot help](/assets/images/posts/sarathi/help.jpeg)

The bot uses `/` as a command prefix and outputs a help string on querying with `/help`.

One observation I've come to make to myself is that the API is quite robust, but the documentation is severly lacking.
However, I feel users of `click` will really grok how this library is written.

### Adding a URL to TIL

![sarathi-bot add URL](/assets/images/posts/sarathi/add-url.jpeg)

To add a new URL to TIL, use `/til add <url> <categories, space separated>`

### Attempting to add a TIL that was previously added

![sarathi-bot add URL same day](/assets/images/posts/sarathi/add-same-day.jpeg)

If you try adding the *same* TIL on the same date, Sarathi will just remind you that you just learnt this.


If you try adding a TIL that exists elsewhere in the database, Sarathi will make note of this in the `repeated_added_on` column.
While this is not yet used, I'd like to analyse whenever I encounter things I have encountered before and think I've not recorded.
It could be a good way of identifying ineffectiveness in how I learn.

### Adding a factoid

Some TILs are just factoids.

![sarathi-bot add factoid](/assets/images/posts/sarathi/add-factoid.jpeg)


### Querying the JSON

To query for a TIL or a couple, just use `/til find <search-string>`. Right now, the search does not support regex, but I plan to integrate that later.
The search string is matched against the categories, or in the URL/factoid body.

![sarathi-bot find](/assets/images/posts/sarathi/find.jpeg)

## Improvements

Some things I'm hoping to integrate in the future:

1. TODO bot to manage my TODO list with a similar file. However, I need to use the VSCode compliant TODO files.
2. Book Bot to interface with my bookshelf's API
3. Book reading progress bot
4. Anki Cards to assist in learning using the TILs and other notes.
5. Interface with my notes repository to auto-generate learning packages.

## Source Code

[You can find the repo to `sarathi` here.](https://github.com/stonecharioteer/sarathi) While very esoteric in its usecase, you might be able to learn a few things about how to use the `discord.py` library from it.
