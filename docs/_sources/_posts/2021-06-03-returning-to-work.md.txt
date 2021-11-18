---
blogpost: true
category: Update
date: June 3, 2021
tags: life, raspberry-pi, work
---
# Returning to the Craft of Programming

I have not been working on side projects in a few months. I've been busy with
life, family, and health. However, I finally feel ready to return to it.

I've been in a bit of a dry-spell regarding side-projects and learning. Sure,
I've put up my [notes website](https://notes.stonecharioteer.com), and I've
finally been a little more disciplined about a blog than I have been, but I
want to return to building things. I haven't taken the Shelfie project beyond a
proof-of-concept, and I'd like to do that.

I've finally setup the ClusterHat 2.2 once again. It's been so long since I
bought it, that I've forgotten that I needed to run `clusterctrl on` to turn on
each individual nodes.

![Raspberry Pi Clusters](/assets/images/posts/raspberry-pi-clusters.jpeg)

And I've installed Unbound on my PiHole last night. That was quite a ride since
it kept messing up my DNS quite a bit. I still don't understand what a
Recursive DNS Server does, though. It seems to continue to ask public DNS
servers about addresses, which is what I assumed PiHole does in the first
place. However, it caches them also? Didn't PiHole do that already? I need to
look into it more.  Perhaps this warrants an entirely separate post.

For now, I'm going to work on installing Hadoop on the ClusterHat. I want to
use this opportunity to learn MapReduce and understand how Hadoop actually
works. I'd also like to shard a postgresql database on them as well, and stress
test them both. I want to keep changing what I use the smaller cluster for.

Let me make a list of things I want to test on this cluster.

1. Hadoop and MapReduce
2. Postgresql sharding
3. Dask
4. Distributed Redis
5. Distributed MongoDB

Alongside these, I also want to do the following:

1. Rewrite the `sarathi` bot.
2. Improve the `til` page, or put it up on a new page, perhaps til.stonecharioteer.com, so that I can use React to build a much more fluid page.
3. Learn Rust and switch to Rust for leetcode.
4. Build a generic PaaS on Rust with a UI in React. The service I want to integrate first is postgresql.

I also have a series of posts on how to write documentation that I want to finish. The entire family came down with Covid so I couldn't get around to it. I'll finish those up this month as well.
