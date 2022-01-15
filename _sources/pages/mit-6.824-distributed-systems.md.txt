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

[MapReduce: Simplified Data Processing on Large Clusters](/assets/documents/pages/mit-6.824/mapreduce-osdi04.pdf)
is the publication that talks about MapReduce and
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

[@1h9m](https://www.youtube.com/watch?v=cQP8WApzIQQ?t=4000s) *Aha!*
So Hadoop came out of a necessity to *facilitate* MapReduce. Google File
System, huh? That makes sense. Having a network file system that enables
splitting a huge file and saving it across servers makes so much sense if you
operate like this. And this also comes with data safety guarantees. Hadoop
naturally has data backup guarantees and replications (3 is default, I think)

[@1h12m](https://www.youtube.com/watch?v=cQP8WApzIQQ?t=4260s) GFS would schedule
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

#### End Thoughts

I like journalling as I watch the course. This way I both concentrate, and
I have copious notes as well. I will rewatch this lecture later, and make
sure that I update my notes. Watch this space.


### Getting the Tests for the Labs

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

### 2020-07-08 Watching Lecture 2: RPC and Threads

#### Golang!

I would *prefer* using Python or Rust to complete this course, but I think
learning Golang to push myself would be a good way to get myself out of this
rut and keep my interest.

Also, the professor taking this course is [Robert Morris](https://pdos.csail.mit.edu/~rtm/).
I love how he teaches. Also, his [pre-MIT papers section is lit!](https://pdos.csail.mit.edu/~rtm/old-papers.html)

It is funny how he says you *could* use Python for this course. But I will avoid
the temptation.

#### Observations on Golang

* Type-Safe
* Memory-Safe
* Garbage-Collected
* The combination of threads and garbage-collection is particularly interesting.
  * You don't need to figure out when a thread was using an object.
* Golang has always been said to be simple. What, 50 keywords?

#### The Golang Tutorial

[@3m](https://www.youtube.com/watch?v=gA4YXUJX7t8&?t=180s) So I am supposed to take the Golang tutorial and then read Effective Go before
I proceed. Will do that.

My friend [Karthikeyan](https://tirkarthi.github.io/) recommended
[Caleb Doxsey's An Introduction to Programming in Go](https://www.golang-book.com/books/intro),
which is available for free at that link. However,
I will shelve perfection and completion in the language (for now),
and [I will focus on the official tutorial.](https://tour.golang.org/)


I am going to store all the code I write for this project on the same github repo as this blog. I might move it later. [Access it here.](https://github.com/stonecharioteer/blog/tree/master/pages/mit-6.824)

In the folder golang, I am going to store all the go code I write
to learn the language. It won't have anything to do with this course, but well.


```go

package main

import "fmt"

func main() {
	fmt.Printf("hello, world\n")
}
```

##### Observations as a Pythonista:

* W00t! I am not writing semi-colons.
* Braces are okay. I can live with those.
* `import` uses *quotes*. I was *just* telling someone about this yesterday.
* [There is an interactive tutorial website!!](https://tour.golang.org/welcome/)
* 2009-11-10 23:00:00 UTC is Golang's Birthday, apparently.
* The way go prints out the timestamp when I use `time.Now()` is so weird. What are those extra numbers? It has the timezone, and that is great. But it also has something akin to `m=+0.00086191`. What is that?
* Every Go Program is made up of Packages?
  * Not everyone realizes that Python is so similar. *Every* python "object" is an "object", complete with its own constructor and all.
  * Note to self: You can preach all the language agnosticism you want, but you cannot take the snake out of the snake charmer's basket.


```go

package main


import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("My favorite number is ", rand.Intn(10))
}
```

Wait. The output is *always* the same! The tour page says this:

> Note: The environment in which these programs are executed is deterministic, so each time you run the example program rand.Intn will return the same number.
> (To see a different number, seed the number generator; see rand.Seed. Time is constant in the playground, so you will need to use something else as the seed.)

Also, so importing `math/rand` allows me to use rand at the global level.

```go
package main


import (
	"fmt"
	"math/rand"
)

func main() {
	rand.Seed(1091234017)
	fmt.Println("My favorite number is ", rand.Intn(10))
}
```

Huh. The output remains constant every time I execute. So true random number
generation is not possible here? I wonder what Python does. I guess it uses
something the timestamp to generate the seed each time. You learn something new!

Go uses tabs! Not spaces. Heh. Pied Piper should have used Golang.

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(math.Pi)
}

```

So Go only exposes those variables that start with a capital first letter?
Works for me.


[Go's types come **after** the variable name.](https://blog.golang.org/declaration-syntax) I like this, to be honest.

Oh wow. That article on declarations is **insane**. I can see why Python's
type hints took the `x: int` form now.

`a, b := 1, 2` seems to be the way to define variable without declaring their
type. The types are implied from the variables on the right. This is not
usable outside of a function since every statement *must* begin with a keyword.

```go
package main

import "fmt"

func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func main() {
	fmt.Println(split(17))
}
```

Naming the return variables allows you to return them implicitly. I am not so
certain I would use that. Cannot see what it is useful. Perhaps in a way so I
can keep track of the returnable variable(s).

Go's types are interesting.

```go
package main

import (
	"fmt"
	"math/cmplx"
)

var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func main() {
	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)
}

```

And the supported types are:

```
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128
```

Go sets initial values to variables. They are either `0`, `false` or `""` depending
upon the type.

Go assignment between items of different type requires an **explicit conversion**.
This is done through the type functions that perform the type casting.


The `:=` and the `var =` ways of declaring variables perform type inferrence,
as noted above.


Go supports immutable `const`s. These can infer types as well. Constants can be character, string, boolean, or numeric values.

#### End Thoughts

I'll be spending another day on this tutorial. There's a lot to cover and
I don't want to rush it. I would like to master enough Go to try going through
the Algorithms course and implementing common algorithms in Go. That would be
fun!

### 2020-07-12 Continuing the Golang Journey

I am taking slightly longer than I hoped for with this. Let me try to finish
it tonight. (Current time is 23:00)

#### Looney Loopy Looping

```go
package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
}
```

Ah, those old C-variety loops. Braces are always required. No parentheses.

Interesting. The `for` can be turned into a `while`-varient by just omitting
the instantiation and the increment.

> C's `while` is spelled `for` in Go,

LOL.

#### Conditionals

Interesting why loops are introduced *before* conditionals. Is it easier to
grok?

```go
package main

import (
	"fmt"
	"math"
)

func sqrt(x float64) string {
	if x < 0 {
		return sqrt(-x) + "i"
	} else {
		return fmt.Sprint(math.Sqrt(x))
	}
}

func main() {
	fmt.Println(sqrt(2), sqrt(-16))
}
```

Hmm. `fmt.Sprint()` does string typecasting, does it?

```go
package main

import (
	"fmt"
	"math"
)

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return lim
}

func main() {
	fmt.Println(
		pow(3, 2, 10),
		pow(3, 3, 20),
	)
}
```

Wait, so `:=` is sort of the walrus operator!! W00t.

### 2020-07-29 The Tour Continues!

Note: *I took quite some time off from this course, but I am back now and I plan to finish this soon.*

So the last time, I was looking at loops. Loops don't need parentheses here. That's good.

```go
package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)

	for sum < 1000 {
		sum += 100
	}
	fmt.Println(sum)

	for {
		fmt.Println("lol infinite loops")
	}
}

```

The initialization and increment are optional, so there is no need for a while or a do-while loop here. Good.

>  [C's *while* is spelled *for* in Go.](https://tour.golang.org/flowcontrol/3)

That's hilarious. If only my old CS teacher Vasanth could see my face now.

[**Go's Conditional's have the *walrus operator*?!**](https://tour.golang.org/flowcontrol/6)

```go
package main

import (
	"fmt"
	"math"
)

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return lim
}

func main() {
	fmt.Println(
		pow(3, 2, 10),
		pow(3, 3, 10),
	)
}

```

I am sold.


The variable defined in the `if` statement isn't accessible outside the statement,
but variables defined within the blocks are accessible outside the blog.
Such a weird decision. I mean, even Python does this but it is very weird.
