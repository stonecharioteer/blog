---
title: Notes MIT 6.824 - Distributed Systems
layout: post
categories: [distributed-systems, learning]
permalink: /distributed-systems.html
description: "Notes on the MIT 6.824 course on Distributed Systems"
customexcerpt: "I began taking the course on Distributed Systems (available for free on YouTube). These are my notes."
---

* table of contents
{:toc}

## Links

1. [YouTube Playlist](https://www.youtube.com/playlist?list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB)
2. [Course Webpage](https://www.youtube.com/watch?v=cQP8WApzIQQ&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB)
3. [Course Schedule](https://pdos.csail.mit.edu/6.824/schedule.html)
4. Course Labs: [1 - MapReduce](https://pdos.csail.mit.edu/6.824/labs/lab-mr.html) \| [2 - Raft](https://pdos.csail.mit.edu/6.824/labs/lab-raft.html) \| [3 - Fault-tolerant Key/Value Service](https://pdos.csail.mit.edu/6.824/labs/lab-kvraft.html) \| [4 - Sharded Key/Value Service](https://pdos.csail.mit.edu/6.824/labs/lab-kvraft.html)

## Motivation

I discovered this course through a comment on HN. I am generally skeptical
about most academic courses on YouTube, but this proved to be really
impressive.

I would recommend having a look at the lab
exercises. *You get to write a **sharded** K/V store!*

I cannot stress this enough. If I am able to **that** by the time
I am done, I will be elated.

On a note, I have not taken any of the apparently required courses
that are listed on the course website, there are no good recordings of [6.033](http://web.mit.edu/6.033/www) or [6.828 - Operating Systems Engineering](https://pdos.csail.mit.edu/6.828/2019/)

## Daily Notes


### 2020-07-07 Watching Lecture 1: Introduction


[Link to the video](https://www.youtube.com/watch?v=cQP8WApzIQQ&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB)

I have never taken study notes like this before, I am typing as I go through
this course. This lecture seems to be focussed on MapReduce. I have *never*
used MapReduce, and I have never really understood what it is and how something
like Hadoop works. I hope to understand it better with this. MapReduce, I mean,
not Hadoop.

#### MapReduce

[MapReduce: Simplified Data Processing on Large Clusters](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf) is the publication that talks about MapReduce and
what it means for computing in general. It is in the required reading.
I will read it after video one.

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
