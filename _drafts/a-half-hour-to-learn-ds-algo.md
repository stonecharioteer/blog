---
layout:    "post"
date:      "2021-01-17 12:10:57.992558"
title:     "A Half Hour To Learn Data Structures And Algorithms"
categories: ['learning']
description: "In which I describe various data structures and algorithms, and take a rather high-level approach."
---

As a self-taught developer, one of my weakpoints is interviewing. I suck at
taking leetcode-style tests, and I am held back by my knowledge of algorithms
and data structures. One of the things I hope to fix is the latter part,
and I hope it will lead to the remediation of the former.

In this article, which will quite possibly delve not further than a high
level into the topic, I will go through all the data structures and algorithms
I've come across thus far in my interview process.

## Data Structures

In programming, a data structure is *something* that holds data and offers it
to the user (*sic.* programmer) in an accessible way. Data Structures are
different tools, to speak of it in a tooling paradigm, and they are often misused
by a developer because they didn't take the time to learn how to use it, or
that such tools are available.

In learning a language, and for this article, I will be using Python, you often
learn the basic constructs that the language offers and don't realize that the
built-in tools can often be used to construct more complex tools.

The reason why you don't to use the *default* constructs as a solve-it-all
macguffin is that it is not always optimal. Sometimes, the way that a particular
data structure offers up its data is not *meant* to be used in the way that
you are attempting to use it.

You might *assume* that this does not matter, so I will be tabulating a bunch
of time metrics for the following operations. To see how I've arrived at these
numbers, you can checkout [this repository](https://github.com/stonecharioteer/python-profile).
While the order of this list is a copy of the tabulated data in
[Problem Solving with Algorithms and Data Structures in Python](https://runestone.academy/runestone/books/published/pythonds/index.html), I've gone about my own way of getting the following graphs and data.


Operation                                                  | Time (for 10 runs) | Time (for 1000 runs) | Time (for 10,000 runs) | Time (for 1 million runs) | Time (for 10 million runs) | Big O Notation
-----------------------------------------------------------|--------------------|----------------------|------------------------|---------------------------|----------------------------|------------------------------------
Indexing a list (`some_list[i]`)                           |                    |                      |                        |                           |                            | O(1)
Indexed Assignment (`some_list[i] = x`)                    |                    |                      |                        |                           |                            | O(1)
Appending to a list (`some_list.append(item)`)             |                    |                      |                        |                           |                            | O(1)
Removing the last item in a list (`some_list.pop()`)       |                    |                      |                        |                           |                            | O(1)
Removing a non-last item in a list (`some_list.pop(i)`)    |                    |                      |                        |                           |                            | O(n)
Insert an item at an index (`some_list.insert(i, item)`)   |                    |                      |                        |                           |                            | O(n)
Delete the list (`del some_list`)                          |                    |                      |                        |                           |                            | O(n)
Loop through the list (`for item in some_list: pass`)      |                    |                      |                        |                           |                            | O(n)
Check if list contains (`item in some_list`)               |                    |                      |                        |                           |                            | O(n)
Get a slice of a list (`some_list[i:j]`)                   |                    |                      |                        |                           |                            | O(k) (Where `k = j-i`)
Set the value of a slice of a list (`some_list[i:j] = 10`) |                    |                      |                        |                           |                            | O(n)
Reverse a list (`some_list.reverse()`)                     |                    |                      |                        |                           |                            | O(n + k) (Where `k = len(some_l))
Concatenate 2 lists (`some_list_1 + some_list_2`)          |                    |                      |                        |                           |                            | O(n)
Sort a list (`some_list.sort()`)                           |                    |                      |                        |                           |                            | O(nlog(n))
Multiply two lists (`some_list * other_list`)              |                    |                      |                        |                           |                            | O(nk) (Where `k = len(other_list)`)

<!-- TODO: Add images and write the profiling script -->


### Linked Lists

Adding an item to a list at a non-final position takes O(n) time. So when you
have a list that is *unordered*, and this order therein, has some meaning to the list,
you'd need a data structure that allows you to add an item *anywhere* in the list
with O(1) time. It becomes especially necessary when you're adding an item *after*
another time.

Think of a bookshelf, for example. You not only want to add a book at the very end
of a shelf, but you might want to place it *next to* another in the shelf, perhaps
a series. If you knew where the reference book was, it makes *no sense* to spend
O(n) time looking for it. That would be like saying you want to *reindex* your
entire bookshelf just to add a new book.

This is where you'd need a Linked List. A Linked List is a data structure
wherein every item knows its predecessor and its successor. Each item is connected
to its *immediate* neighbours.


```python
class LinkedList:
    """Linked List class definition"""
    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head

    @head.setter:
    def head(self, head)
        self._head = head

    def is_empty(self):
        return self._head is None

    def add(self, item):
        """Adds an item to the top of the list."""
        temp_node = Node(item)
        temp_node.next = self.head
        self.head = temp_node

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def find(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return current
            else:
                current = current.next
        return None


class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self) -> Node:
        return self._next

    @next.setter
    def next(self, value: Node):
        self._next = value
```


### Stacks

### Queues

### Trees

### Graphs

## Algorithms

### Sorting

#### Bubble Sort

#### Quick Sort

#### Insertion Sort

#### Merge Sort

#### Heap Sort

#### Tim Sort


### Searching Algorithms

#### Linear Search

#### Binary Search

### Dijikstra's Shortest Path Algorithm
