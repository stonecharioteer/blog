---
title: Notes on MIT 6.824 - Distributed Systems
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

[@1h9m](https://www.youtube.com/watch?v=cQP8WApzIQQ?t=4000) *Aha!*
So Hadoop came out of a necessity to *facilitate* MapReduce. Google File
System, huh? That makes sense. Having a network file system that enables
splitting a huge file and saving it across servers makes so much sense if you
operate like this. And this also comes with data safety guarantees. Hadoop
naturally has data backup guarantees and replications (3 is default, I think)

[@1h12m](https://www.youtube.com/watch?v=cQP8WApzIQQ?t=4260) GFS would schedule
the map task *where* the data chunks were for network efficiency? That makes
sense because the map job packet size must be *much lower* than the data that
it operates on. This is good. Helps me understand what the heck is going on
with Hadoop.

Map stores its output on the disk of the machine that it executes on. But to
group together all the values associated to a key and then to **reduce** them
on a separate machine, they need to be moved later. So the row-wise data of say,
words in a word count dictionary, would have to be converted to a columnar
dataset of words and their counts as opposed to a collection of different words
and their individual counts across different files.

Say:

```python
# again, don't try to run this.


map_output_1 = {
    "cat": 10,
    "dog": 20
}

map_output_2 = {
    "elephant": 2,
    "dog": 29
}
```

This would then need to be turned into *3 reduce jobs*. One for the key "cat",
one for "dog" and one for "elephant" across these two outputs.

Huh. How would you do sorting in MapReduce? Wouldn't you need to know where
something would appear? Perhaps split large arrays and sort sections and then
sort those again? There was an algorithm for that, I think. I had watched
some animation that showed this.

<!-- TODO: add link to that video. -->


Chaining together MapReduce seems to be a normal procedure. I suppose sorting
could operate like that.

### End Thoughts

I like journalling as I watch the course. This way I both concentrate, and
I have copious notes as well. I will rewatch this lecture later, and make
sure that I update my notes. Watch this space.


## Getting the Tests for the Labs

[Ugh, the CSS in the Labs pages is so horrible for accessibility.](https://pdos.csail.mit.edu/6.824/labs/lab-mr.html) I cannot
read the code snippets either. I love the course, but whoever made the webpages
did not care a bit about accessibility or design of an interface.


```bash
git clone git://g.csail.mit.edu/6.824-golabs-2020 6.824
cd 6.824
```

I've cloned this repo. Apparently this one lecture is enough to get started.
The course does recommend golang, but I am going to try some rudimentary
stuff with Python, and I will get around to golang later, once I learn it.
