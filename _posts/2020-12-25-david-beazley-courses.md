---
blogpost: true
category: Review
date: Dec 25, 2020
tags: learning, python, computer-science, courses, covid
permalink: dabeaz.html
---
# David Beazley's Courses

Among other things, 2020 has been a window into opportunities I didn't have
before. Mostly with respect to time. I was able to rest, which given my
penchant for workaholism, was something my mind deserved. I was also about to
heal from burnout and come to terms with my job, which I'd just started in
2019. I needed the time to recharge, and ignore all the expectations I had set
for myself professionally. I have been overwhelmed with immense Imposter's
Sydrome, and I needed a chance to get over it.

In June, I discovered that David Beazley, someone whose talks at PyCon I
constantly recommend, began offering his hitherto in-person courses, held in
Chicago, online. Dave's courses were *interesting* to someone like me who
doesn't have a formal Computer Science degree. *Interesting?* I am underselling
here. One course aimed to help you write a *Compiler* in a week! I didn't know
a thing about lexical parsing, let alone what would be the "Hello World"
equivalent in Compiler writing.

I don't remember *how* I found out that he was offering his courses online. I
suspect it was a tweet. So I reached out to him and he added me to a slot for
the next, upcoming course.

## The Structure and Interpretation of Computer Programs

The [MIT Course 6.001 - Structure and Interpretation](https://www.youtube.com/watch?v=-J_xL4IGhJA&list=PLE18841CABEA24090)
is an *insane* way to introduce computer programming to someone. The
accompanying book is even more so. In today's day of teaching kids to code
using the BBC MicroBit, some Python, or heavens forbid, Javascript, is
well-advertised. But you *could* slap the SICP book on someone's study table
and say "Read this, and you will be a programmer, my child." Sure. You *could*
do that. In fact, hit me up if you manage to get a child to read that book. I
want to meet such a child.

[Dave's course](http://dabeaz.com/sicp.html) attempts to get you through the
book in 5 days. "That's *mad*," I said to myself. And *of course*, I wanted in.
I'd heard of SICP a while ago, but I treated it as this untouchable classic,
one that I couldn't fathom without an innate understanding of Lisp.

(And Lisp (as you should know by know) is a (very) harrowing experience for
something who has coded (mostly, (ignoring some work in Node and React)) in
Python.)

I enrolled for the SICP course, which Dave held from Fri Aug 14 8pm - Sat Aug
15, 2020 4am. No, the time wasn't a mistake. That was the time he was
conducting it converted to Indian Standard Time.

I was in for an interesting week!

Dave's courses are *amazingly well organized*. He is coordinated, and there are
absolutely no zoom hiccups.

The timeline is as follows:

1. You checkout [his website](https://dabeaz.com) and figure out which course,
   and the appropriate schedule you'd like to enroll for;
2. You email Dave and ask him to enroll you.
3. Dave sends a confirmation and sends you an invoice.
4. You complete payment, (there are no follow-ups regarding the payment) and
   you get time till upto 2 or 3 weeks before the course starts.
5. Dave emails you a week before the course starts, asking for your github ID
   so he can give you collaboration rights to a private github repo.
6. He also adds you to a Gitter.im channel, so you can chat with others in the
   course.
7. You also get a zoom invite, and you can join in on the day of the course.

During the course:

1. Dave spends batches of 30 minutes to an hour to discuss and explain theory,
   and concepts.
2. The rest of time is spent coding and working on exercises.
3. Everyone codes on their own branch, and we get to see each other's work.
4. On some days, Dave splits everyone into breakout rooms wherein you can
   discuss the current work, and Dave swings by to check in on you. Sometimes,
   the breakout room is a chance to just ask Dave questions.

The SICP course is conducted using Racket, but you could choose to do the
coursework in any Lisp-flavoured language. Racket is an interesting language,
in that it tries its best to make itself beginner-friendly.

Dave covers roughly 1 chapter a day in those 5 days, and he encourages you to
work on most of the exercises, working on them himself through screenshare. I
wonder how much Dave dreams in Racket now. I should ask him this on twitter
sometime.

I thoroughly recommend everyone who has the chance to take this course, even if
you're never going to code in Lisp-flavoured languages ever again. At the very
least, you will walk away with an appreciation for recursion that you cannot
gain easily in such a short time.

## Write a Compiler

[The compiler course](http://dabeaz.com/compiler.html) was something I was
*really* looking forward to. I have been very interested in how things like
LLVM work, and how you'd go about writing a silly programming languuage.

The structure of the course is very custom. Dave helps you work through
implementing a language called Wabbit. I hope one day I can pay Dave back for
the experience and write an emacs linter for Wabbit. I'd call it Fudd, perhaps.

Dave's course helps you begin to understand how to write your own language, and
he does this using Python. The most interesting questions pile up when you are
working on this course, because at the beginning, you are not privvy to the
bigger picture. The first time you actually run and compile your first Wabbit
program, it will, forgive the Christmas metaphor, feel like the first taste of
warm homemade cookies on Christmas eve.

A Sidebar in how amazing this course is, is that one of the people who attended
the batch with me was Naomi Ceder, who was also one of the Keynote speakers for
PyCon India 2020.

I recommend the Compiler course to anyone who is interested in understanding
how a language translates to machine code, and how you go about optimizing your
language's design. You learn things like how to go about designing language
constructs, and you gain an appreciation for how your favourite language is
implemented.

I enrolled in the September 14-18 batch.

### RAFTing Trip

[The RAFT Distributed Consensus Algorithm](http://dabeaz.com/raft.html) was the
first of the courses that I actually needed for work. I wanted to understand
how a distributed system actually works under the hood.

> It's AppendEntries, it's all AppendEntries.
>
> \- Dave

Dave's course on RAFT is a great way to understand how something like `etcd`
works. [The RAFT paper](https://raft.github.io/) is a tough read, and though it
isn't as convoluted as the Paxos paper, it has a few doozies that become
apparent only during implementation. In fact, attending this course makes me
wonder if you could form a country using the LeaderElection rules.

A prerequisite for this course is some knowledge of Socket Programming in
Python. Dave does spend some time teaching you how to use the socket library,
but I'd recommend coming after doing some homework. It will help you spend more
time in understanding the paper and asking Dave questions.

I attended the Sat Dec 5 9pm - Sun Dec 6, 2020 5am batch for this course. DST
pushed the course 1 hour further, and I made sure I was fuelled with a lot of
coffee. My main objective was reading the paper, and while I couldn't follow
some implementation details since I was not too focussed on implementing RAFT
in python, I was having fun watching the others in the course attempt to do so
using Elixir, Rust Python and Racket.

Of the three, I am having a hard time picking a favourite, since each is a
unique kind of fun. These are not *easy* courses, mind you. You will need to be
off work for a week, and you will need to up your coding game. However, the
courses are bolstered by how approachable Dave is, and how fun it is to watch
him code and build what appears to be insane in a week. Sure, he's done this a
lot before, but you can see how much work has gone into this course.

### Conclusion

To the reader, if you're considering taking his courses and don't know where to
start, the order in which I covered it is pretty approachable. If you want to
up your Python game, I'd also recommend his
[Advanced Python course,](http://dabeaz.com/advprog.html) which I didn't take
up this year since I wanted to get these out of the way first. If you want to
checkout some of Dave's talks, or his free Python Programming course, check out
[his website.](http://dabeaz.com)
