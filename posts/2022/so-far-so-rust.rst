:blogpost: true
:date: Jul 13, 2022
:category: Tech
:tags: Rust

.. _so-far-so-rust:

=============================
So Far So Rust
=============================

I've been using Rust as my primary programming language for 145 days now.
In this article, I'm going to discuss my journey so far.

While I've talked about this at length to my friends and even at meetups, I
haven't written about Rust as much as I'd like to. I came into this language the
same way as I did to Python: sheer gut feeling. While I was considering Ruby
instead of Python, here my alternative was Golang. Back then, I wasn't educated
enough to make a decision so I left it to a friend who recommended I choose
Python. Today, that choice oddly involved the same friend who's been using Rust
at work. However, it also stemmed from a gut feeling that I wanted to learn Rust
and not Golang for my side-projects.


.. admonition:: An Aside
   :class: tip

   A funny thing about my journey with Rust and Ruby is that `Steve Klabnik
   <https://steveklabnik.com/>`_ is involved in both of them. I chose Python
   over Ruby, and Steve is one of the most prolific contributors to Ruby on
   Rails. And I chose Rust over Golang, and was mildly surprised to find that
   Steve is involved with Rust and is one of the co-authors of the defacto book
   on the topic.

   Another fun fact is that `Armin Ronacher, <https://lucumr.pocoo.org/>`_ the
   creator of Flask, my favourite Web Framework, also shifted to Rust. In fact,
   `Armin's talk at PyCon India 2018
   <https://www.youtube.com/watch?v=-4fzFKihmJw>`_ convinced me that my gut
   feeling about Rust was right.

How did I go about learning Rust? As someone who's only coded in Python and a
little bit of Javascript, I didn't have much of an understanding of low-level
programming constructs such as memory management to really grok stuff at the
beginning. The advice most newbies get is "read The Book", and while that is
great advice, I kept faltering when trying to read it. I wanted to get my hands
dirty ASAP and I wanted to build something that I could use.

.. note::

   Rust has the reputation of being a Systems Programming Language.
   While the language did originally target itself as being an accessible
   systems language, the home page now says this instead.

   |     *A language empowering everyone*
   |     *to build reliable and efficient software.*

   Don't let the systems programming language tag scare you. Rust is designed to
   be used everywhere.


The opportunity came at work when I needed to build a health-check endpoint atop
of our data services at Merkle Science. The original requirements needed me to
hit our internal APIs and measure latency in realtime, and the prototype had
been written in Python. It was introducing latency of its own and clearly that
was an effect of the way it had been written. I could have rewritten it so that
it stayed in Python, but that felt like a perfect reason to use Rust. I needed
to write a webservice, so I sought the framework that looked the most like
Flask, my preferred web-framework of choice: Rocket. In retrospect I was thrown off the
more popular choice in Rust, actix-web, because I *thought* I had to use the
actor-framework model that actix came with. Surprisingly, I learnt a long time
later that actix-web doesn't use actix under the hood anymore. The names are an
unfortunate left-over from when the projects stemmed together. However, Rocket
was easy to understand and I liked what I saw.

The funny thing about how I started Rust is this. I'd been trying to learn it
for months and I came upon a book called `Rust Web Programming by Maxwell Filton
<https://www.packtpub.com/product/rust-web-programming/9781800560819>`_ and
began reading it. I didn't complete the book, but the first two chapters gave me
more than enough to try writing code on my own. Another resource I found helpful
earlier was `A Half-Hour to Learn Rust
<https://fasterthanli.me/articles/a-half-hour-to-learn-rust>`_, by Amos Wenger.

.. note::

   These resources worked for me, but again, **read** `The Book
   <https://doc.rust-lang.org/book/>`_, which is the *definitive* resource for
   newbie Rustaceans. I am working my way through the book now, and it teaches
   me a lot that I wish I knew earlier.

I had seen the trait system at work, and wanted to use it for my task, since it
involved hitting similar APIs which all had their own nuances, while returning a
synonymous result. I wanted to create a trait that all the checks would
implement, so that it would be extensible later down the line.

After trying to write a little rust for a few days, I decided to tackle the
`Rustlings course <https://github.com/rust-lang/rustlings>`_, which provide
interactive exercises for you to follow along. I solved all of them over a
period of 3 days and I had to google for the answers to some of them. In
particular, I recommend the exercises on strings to really grind some of the
basics into your brain.

While trying to grok how strings work in Rust, my friend recommended the `Let's
Get Rusty <https://www.youtube.com/c/LetsGetRusty>`_ YouTube Channel and, in
particular, the `video on Strings
<https://www.youtube.com/watch?v=Mcuqzx3rBWc>`_.

After going through these resources, I began building my service and encountered
a few gotchas that seem trivial today.

- I couldn't return a string slice from within a function because it was created
  inside the function and essentially points to something that no longer exists.
- Async functions could be called from within a synchronous functions as long as
  I wrap them inside a blocking runtime, such as the one offered by the `futures
  <https://docs.rs/futures/latest/futures/>`_ crate or the `tokio crate
  <https://tokio.rs/>`_
- To implement something I'd take for granted in Python, such as a retrying
  mechanism, I'd have to understand *how* to write a function that returns a
  generic response. This is :ref:`something I've documented here.
  <rust-reqwest-retry>`

There are a few more gotchas that I ran into, especially when it came to
something as simple as the ``return`` keyword.

When I first started learning Rust, the fact that a function could be written
like below, stumped me.

.. code-block:: rust
   :linenos:

   fn add_ten(x: i32) -> i32 {
      x + 10
   }

Where's the return statement? Turns out Rust ``blocks`` all operate this way. A
block can *evaluate* to some value, and you could also write code like this.

.. code-block:: rust
   :linenos:

   fn add_ten(x: i32) -> i32 {
      let result: i32 = {
         println!("I'm going to add 10 to {x}");
         x + 10
      };
      result
   }

The ``block`` that contains the ``println!`` statement and its subsequent line
*evaluates* to ``x+10``. Take this in for a second. Every single statement you
will see eventually runs on this simple assertion. Match statements, ``if-let``
statements, or even a simple block like above that's only written this way to
show you what you *could* do, all of them can evaluate to a result.

And the type annotations can coerce functions that use generics to return
appropriate values.

.. note::

   Rust is the first strongly typed language I have used, so forgive me if I
   sound like a fanboy when it comes to this. I have serious beef with Python's
   type hints, and how it's just a hint and nothing more. I *love* how Rust
   handles types and how constraining it feels, just so that I can use these
   constraints to not only *be a better developer*, but also to control my
   program from going haywire.

One of the things I've learnt writing Rust as opposed to Python is that my code
fails, frequently.

I wrote a crawler to get data out of a paginated API, and my code had to account
for edgecases pretty early on. The structs I wrote to deserialize payloads would
fail at the first hint of a mismatch, especially when it came to types. I needed
to know what *could* be a null value and what wouldn't be. I needed to know the
exact format for a timestamp and how to parse it.

Other things about Rust seemed to be harder to grasp. The import system was
something else that I really struggled with.

.. code-block:: Rust
   :linenos:

   use std::env;

   fn main() {
      let value = env::var("SOME_ENVIRONMENT_VARIABLE");
      match value {
         Ok(v) => println!("SOME_ENVIRONMENT_VARIABLE = `{}`"),
         Err(e) => eprintln!("Error: {e:?}");
      };
   }

In this above block, I *assumed* the ``use std::env`` line was an *import
statement. I was blissfully unaware that I didn't *need* to import something
like this. I could, instead, have written it like follows.

.. code-block:: Rust
   :linenos:
   fn main() {
      let value = std::env::var("SOME_ENVIRONMENT_VARIABLE");
      match value {
         Ok(v) => println!("SOME_ENVIRONMENT_VARIABLE = `{}`"),
         Err(e) => eprintln!("Error: {e:?}");
      };
   }

The ``use`` keyword wasn't synonymous with Pythons ``import`` keyword. It was
more akin to ``import requests.client as client``, bringing something into my namespace so
that I didn't need to constantly refer to the entire import resolution path.

When I didn't know this, using the ``env_logger`` `crate <https://docs.rs/env_logger/latest/env_logger/>`_ was unnerving.
I didn't know if Rust was injecting ``env_logger`` into my namespace somehow. It
made me really uncomfortable because I hate having variables in my namespace
that I didn't control.

However, Rust was doing something else. Every crate was available to use, if I
didn't want to ``use`` it, I could have just written out the entire import path.

Those are not all of the gotchas, though. I continue to run into them every day,
but you get the idea.

Today, I'm using Rust in two projects at Merkle Science. First is the health
check application I mentioned, while the second is a data-ops CLI that I wrote
to help us load data into our datastores.

-----------------------------------
Choosing Rust - A Retrospective
-----------------------------------

This article has been about *how* I learnt Rust, and trust me, there's a lot
more to say about that. My advice is pick a problem you'd choose any language
for and choose Rust to solve it. Remember that it will take you longer, not just
at first, than it would in a language like Python or Javascript. I don't even
profess to know that you'll get guaranteed benefits, but what I *can* tell you
is that you will learn new things; new **paradigms.**

I chose Rust because I *felt* like I wanted to code in Rust. I don't claim to
have a performance or memory-safety related answer to you. I've been falling
slightly out of love with Python, largely because of the state of its virtual
environments ecosystem or the "ship your development machine" gimic that
containers seem to inculcate into every developer.

Rust is fun. I've had so much fun coding in Rust that it reminds me of how much
fun Python used to be. I am glad I can use it at work, and I am glad I can use
it for my side projects. It's a language that feels fresh, and coding in it has
taught me so much already.

1. I have learnt how to think about the mutability of my variables.
2. I think a lot more about the *types* of my variables and the scopes they live
   in.
3. I have learnt a lot about accounting for errors in my code. ``Result`` is
   *amazing*.
4. ``Enums`` are mind-blowingly amazing.
5. Pattern matching is just *chef's kiss.*

All of this being said and done, I don't know if Rust is for *you*. Perhaps
Golang is. There's no reason to try both. I did, and I still don't have a
problem with Go. I prefer Rust, that's all. If you're trying to look for a job,
I don't recommend Rust. There are so few jobs out there for you. If you're
trying to rewrite your codebase for performance, let me tell you that you might
be able to do it in the language of your choice. Look into distributed
programming patterns, or even see if you can learn to profile and DRY your code.
Learn to use caching and memoization. Improve your algorithms and
datastructures. At times, your code might not even be the bottle-neck; for most
web-applications, it's your database queries. Don't use an ORM blindly. Learn
how SQL's ``EXPLAIN`` statement works, you will build more efficient web
applications with ease.

Sometimes, a shell-script does everything you need a fancy CLI to do. So do
that instead.

However, should you choose Rust, great job. You will struggle for a while, I
know I do even today, but you will also be able to build an amazing application
because you're closer to the metal. You will enjoy not having to install
``build-essential``, or other build-time dependencies on your production
machine. You don't need to install ``libgit`` or those pesky ``openssl``
libraries either. Your compiled application has everything it needs.

Rust is fun. Get used to the compiler shouting at you, because it's a good
teacher.

-----------------------
Resources
-----------------------

.. note::

   I'll update this list as and when I get a chance or come across something
   that helps me learn a newer concept.

While I used some pretty nondescript resources to learn Rust, I don't recommend
you do the same. At the time I began, a lot of the below resources didn't exist,
so I didn't have an opportunity to use them. However, I recommend you go through
these instead of following my path.

Books
========

1. `The Rust Programming Language by Steve Klabnik & Carol Nichols <https://doc.rust-lang.org/book/>`_
2. `Rust for Rustaceans by Jon Gjengset <https://nostarch.com/rust-rustaceans>`_
3. `Zero to Production in Rust: An Introduction to Backend Development by Luca
   Palmieri <https://www.zero2prod.com/index.html>`_
4. `Rust in Action by Tim McNamara <https://www.manning.com/books/rust-in-action>`_
5. `Programming Rust by Jeff Blandy, Jason Orendorff & Leonara F. S. Tindall
   <https://www.oreilly.com/library/view/programming-rust-2nd/9781492052586/>`_

Podcasts
=========

1. `New Rustcean <https://newrustacean.com/>`_ (discontinued)
2. `Rustacean Station <https://rustacean-station.org/>`_

Youtube Channels & Video Compilations
=======================================

1. `Let's Get Rusty <https://www.youtube.com/c/LetsGetRusty>`_
2. `Jon Gjengset <https://www.youtube.com/c/JonGjengset>`_
3. `Bryan Cantrill's Talks <http://dtrace.org/blogs/bmc/2018/02/03/talks/>`_

Videos
==========

1. `Type-Driven API Design in Rust by Will Crichton at StrangeLoop
   <https://www.youtube.com/watch?v=bnnacleqg6k>`_
2. `Rust: A Language for the Next 40 Years by Carol Nichols
   <https://www.youtube.com/watch?v=A3AdN7U24iU>`_
3. `Error Handling isn't all About Errors by Jane Lusby at RustConf 2020
   <https://www.youtube.com/watch?v=rAF8mLI0naQ>`_
4. `How to Learn Rust by Tim McNamara at Rust Linz Meetup
   <https://www.youtube.com/watch?v=sDtQaO5_SOw>`_
5. `Learning Systems Programming with Rust by Julia Evans at RustConf 2016
   <https://jvns.ca/blog/2016/09/11/rustconf-keynote/>`_

Blog Articles
===============

1. `A Half-hour to Learn Rust <https://fasterthanli.me/articles/a-half-hour-to-learn-rust>`_
2. `Sustainability with Rust - AWS <https://aws.amazon.com/blogs/opensource/sustainability-with-rust/>`_
3. `Rust for Python Developers by Armin Ronacher <https://lucumr.pocoo.org/2015/5/27/rust-for-pythonistas/>`_ (2015)
4. `You Can't Rust That by Armin Ronacher <https://lucumr.pocoo.org/2018/3/31/you-cant-rust-that/>`_ (2018)
5. `Rust Tips and Tricks by Jon Gjengset <https://thesquareplanet.com/blog/rust-tips-and-tricks/>`_ (2018)

Others
========

1. `Roguelike Tutorial In Rust <http://bfnightly.bracketproductions.com/>`_
2. `Command Line Apps in Rust <https://rust-cli.github.io/book/index.html>`_
3. `Asynchronous Programming in Rust <https://rust-lang.github.io/async-book/>`_
4. `The Rustonomicon <https://doc.rust-lang.org/nomicon/>`_
5. `Rust Design Patterns <https://rust-unofficial.github.io/patterns/>`_
6. `The Little Book of Rust Macros <https://danielkeep.github.io/tlborm/book/index.html>`_ (WIP)
7. `Rust by Example <https://doc.rust-lang.org/rust-by-example/>`_
8. `Rustlings - Interactive Exercises to Learn Rust <https://github.com/rust-lang/rustlings>`_
9. `The Cargo Book <https://doc.rust-lang.org/cargo/>`_
10. `StackOverflow - What are the differences between Rust's \`String\` and \`str\`? <https://stackoverflow.com/a/24159933/18407535>`_
11. `The Relative Performance of C and Rust by Bryan Cantrill <http://dtrace.org/blogs/bmc/2018/09/28/the-relative-performance-of-c-and-rust/>`_
12. `Writing an OS in Rust <https://os.phil-opp.com/>`_
