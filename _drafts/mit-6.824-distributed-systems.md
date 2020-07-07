---
title: Notes MIT 6.824 - Distributed Systems
layout: post
categories: [distributed-systems, learning]
description: "Notes on the MIT 6.824 course on Distributed Systems"
customexcerpt: "I began taking the course on Distributed Systems (available for free on YouTube). These are my notes."
---

* table of contents
{:toc}

## Motivation

I discovered this course through a comment on HN. I am generally skeptical
about most academic courses on YouTube, but this proved to be really
impressive.

The course website is here, and here's the schedule that is suggested. I would
recommend having a look at the lab exercises. *You get to write a **sharded** K/V store!*

I cannot stress this enough. If I am able to **that** by the time I am done,
I will be elated.

## Daily Notes


### 2020-07-07 Watching Lecture 1: Introduction

I have never taken study notes like this before, I am typing as I go through
this course. This lecture seems to be focussed on MapReduce. I have *never*
used MapReduce, and I have never really understood what it is and how something
like Hadoop works. I hope to understand it better with this. MapReduce, I mean,
not Hadoop.

#### MapReduce

So MapReduce is essentially splitting a problem into smaller sets based on some
criteria, and then assembling the solution from partial solutions. Map a function
onto a list of inputs, and then *reduce* the results into solutions.


The example he shows is a word count functionality. Given a set of files,
how would you give a word count across them?


```python
# this isn't executable code btw. Just me thinking out loud.
def map(key, value):
    files = value
    for file in files:
        for word in file:
            yield word, 1

def reduce(key, value):
    yield len(value)

```

The way this would work is:

1. The map function would return something like a dictionary in python terms,
   and it would have perhaps the file name, and then a data structure that has
   the word and its count in this file.
2. The reduce file would use all these outputs, and then *mush* them together
   by returning another final result that has the *overall* solution.

So this could be scaled by splitting the problem *across* CPUs or *machines*
themselves.

Makes sense. I guess that is why it is used with Hadoop. Hadoop is a joint
filesystem that enables such a mechanism, especially when you'd need to process
actual *files*.
