:blogpost: true
:date: Jan 16, 2022
:category: Tech
:tags: Teaching, Documentation, Developer Relations

============================================
Documentation Without Assumption
============================================

Whenever you write documentation, always try to focus on your audience. I've
written about this (in my embarassingly half-complete idea about documentation),
and I'm always going back to this. Documentation is about caring. I see a lot of
developers who don't write good documentation. But what *is* **good**
documentation?

There are many ways of saying the same thing. It's something we take for
granted, really.

Consider the following set of instructions:

1. Log in to the Neo4j server and import the dataset from PostgreSQL.
2. Run this query (included as attachment)
3. Ensure data is uploaded.

I've seen variants of these instructions, oftentimes accompanies by code or
script snippets that a newcomer would look at with a blank face. To an
experienced engineer, would this seem obvious?

No. It would not.

Consider the following questions for a moment.

1. What is the IP address of this server?
2. What credentials do I have to use to login?
3. What roles would I have to be added to, so that I can login?
4. How is the neo4j service running?
5. Is this a production database? Do I risk bringing a system down by running
   thise query?
6. What do I do if the import fails midway? Is there a session configured or do
   I have to figure out where the import failed and then write a query to import
   from there?
7. What is the IP of the PostgreSQL Server?
8. Which Dataset am I importing?
9. Again, creds and accesses for this database?
10. Are there time slots when I *should* not run this query?
11. Should I be recording this?
12. Is there nothing I should change in your query script? Are there any
    variables in the script I need to change, if so, what are the possible
    values?
13. What measures the data consistency or the success of the upload?
14. How should I record the result of that check? Is there a physical (or
    digital) record or is it a "sure, I did this", sort of record?

Go through those instructions once again and read all these questions. While
the instructions might *seem* like they're given without context, and that you'd
have much more context for real instructions, I'm afraid such an assumption is
wrong. And it doesn't matter if you're at a startup or at a large organization.
Lack of assumption-free documentation, with clarity, is scarce. I've not seen
documentation that has yet impressed me at organizations. And this is odd.

One of my favorite resources on writing documentation is the `Divio Documentation
System. <https://documentation.divio.com/>`_ I implore everyone to read it. But
again, documentation is about caring. Far too few developers care about their
work. It's either "I'm too busy", or "I have bigger fish to fry", or "I'm not
going to write docs because you can read the code."

No. If you're not writing documentation, your code isn't going to be quite that
readable either. And no, documentation doesn't take more time. In fact, it
speeds up the process because you have an idea of what you're doing. Especially
when you document everything with excruciating detail.

**State the obvious**. Assume that the obvious is never really obvious. Write
documentation so that you can leave the company at any point of time and no one
will need to contact you to ask you what this function does or how to follow
these instructions. If that makes you feel you're replaceable and your job is at
risk, don't let it. Instead think of it as proof that you're valuable, because
the way you work is the way everyone should: with care.
