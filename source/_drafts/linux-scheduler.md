---
title: The Linux Scheduler
layout: post
categories: [linux, advanced]
description: "How does the Linux scheduler work?"
customexcerpt: "My friend asked me a question that got me thinking... How does the Linux scheduler work?"
---

I have not had a great foundation in Computer Science. I have meandered around
full stack application development, and my friend Sumanth pointed out that I
needed to improve this gap in my education. So he asked me a question that got
me thinking:

> ### How *does* the Linux Scheduler work?
>
> You are running a process `pidx` how does your computer end up picking up
> another process?
>
> What decides how this happens?
>
> What is the minimum duration you can sleep?
>
> How accurately can you invoke sleep for the duration you want?
>
> Exercise: Increase/decrease the time slice in your kernel and see how your computer behaves.
>
> Look into CPU governors so you can learn how to improve a laptop's battery life using this knowledge.
>
> Protip: Look into the following:
>
>   1. Preemption (Computing)
>   2. Iterrupts
>   3. Timers
>   4. Ticks
>   5. Time Slices

I have no idea how to do this so I'm going to search the internet for the
phrase "Linux Scheduler" and "Linux Scheduler Hackernews".

## References

1. [Linux Kernel Documentation](https://www.kernel.org/doc/html/latest/scheduler/index.html)
2. [The Linux Scheduler: a Decade of Wasted Cores](http://www.ece.ubc.ca/~sasha/papers/eurosys16-final29.pdf)
3. [Discussion on the above paper](https://blog.acolyer.org/2016/04/26/the-linux-scheduler-a-decade-of-wasted-cores/)
4. [My Fork of the Linux Scheduler and the Paper associated with it.](https://github.com/stonecharioteer/LinSched)


## Preliminary Study

### Reading the Linux Kernel Documentation on the Scheduler

*Boy this entire documentation is so disorganized.* There should be an introduction manual to the
manual.
