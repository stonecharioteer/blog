---
title: Python Closures
layout: post
categories: [python, tutorial]
description: "An article about closures in python, and how decorators facilitate them"
customexcerpt: "I wanted to take a moment to dive into closures in python, and what they do."
---

## Preamble 

About a year ago, a friend and I were discussing closures in programming languages,
and how they were treated so specially in many technical circles.
To us, the concept seemed weird. Python's closures were... *intuitive*, weren't they?
Both of us were not exactly from a standard programming background, but we were (and still are) super passionate about tech.

Which is why we were confused. Whatever it is that the world calls **closures** seems pretty obvious. At least to us they were.

And well, we weren't wrong. But we were mildly surprised at how Python deals with it.

## Intended Audience

This is an intermediate level article, and you might be confused reading it if you don't understand the following:

1. [Writing Python scripts.](https://docs.python.org/3/tutorial/index.html)
2. [Using the REPL Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
3. [Writing functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
4. [Writing classes (knowledge of inheritance is not required)](https://docs.python.org/3/tutorial/classes.html)
5. Using the [`id`](https://docs.python.org/3/library/functions.html#id), [`help`](https://docs.python.org/3/library/functions.html#help) and [`dir`](https://docs.python.org/3/library/functions.html#dir) functions.
6. [Using the `dis` module to disassemble Python code.](https://docs.python.org/3/library/dis.html)

I have linked to the best articles (IMO) on these topics above, so if you like, you can go ahead and read those first.

Also, most articles deal with an article with respect to nested functions. While I *do* deal with nested functions, I do not start there. I start earlier, with a simple variable,
and build up to nested... let's say objects.


## Introduction

Let's take a look.


```python

def some_func():
    something_to_return = 10
    print(f"id(something_to_return) = {id(something_to_return)}")
    return something_to_return
```

The `id` function in Python is a built-in that [returns the *identity* of the object the variable.](https://docs.python.org/3/library/functions.html#id)
I use this function to sniff around my code to see if I am passing around copies of a variable or if I am actually passing the variable (*sic* object) itself.

In this case, it is easy to test this theory.


```
>>> x = some_func()
id(something_to_return) = 10917664
>>> id(x)
10917664
```

Of course this number will vary, and it could be the same, but for objects with non-overlapping lifetime.
In other words, during one specific *scope*, these numbers are guaranteed to be representative of a specific object.

## Scopes

The *scope* that I just brought up is, in very simple terms, like a space for your code to run in. In python, variables are shared from an outer scope to an inner
scope.


```python

def test():
    x = 10

print(x) # This will result in a NameError exception since x was defined inside a function.

test()
print(x) # no, calling the function doesn't add whatever is inside magically to the "higher" scope"
```

A higher scope is indicative of a scope that contains another scope. If that is too wordy for your taste:

```python

# this is scope 0
def func():
    # this is scope 1
    def func2():
        # this is scope 2
        pass
    pass 
```

In this example, scope 0 *contains* scope 1. Scope 1 *contains* scope 2. However, everything in scopes 0 and 1 are accessible in scope 2, and everything in scope 0 is accessible to scope 0.

Scope 0 is the outermost scope. Scope 1 is inside scope 0. Scope 1 is outside of scope 2. Scope 2 is inside scope 1.

This will become clearer in time.

## Sniffing around returned values

Now, let's look back at our closures. We saw that the `id` value of the integer that was returned is the same. which means, technically, that the same object was returned into the outer scope from the inner scope.

Let's expand this example.

```python

def func():
    x = 10
    print(id(10))
    return x

external_x = func()
print(id(external_x))

def func2(inp):
    print(id(inp))
    return inp

external_inp = func2(external_x)
print(id(external_inp))
assert external_x is external_inp, "The item is not the same. This assertion should not have been raised"
```

When I run the above snippet, here's what I get:

```
94093123237024
94093123237024
94093123237024
94093123237024
```

If you are following along, this means that the application passed around a variable `x`, created *inside* `func`, outside of its scope, and then *into* the scope of another function that returned it unmodified, and the `id` was never changed. This means that all through your process, you passed around a single object. You did not change it.

Now, you might wonder if this would work.

```python
def func():
    x = 10
    print(id(x))
    return x

ext_x = func()
print(id(ext_x))

def func2(inp):
    inp = inp**2
    return inp

ext_x2 = func2(ext_x)
print(id(ext_x2))
assert ext_x is ext_x2, "the objects are not the same"
```

When I run this, here's what I get:

```
94093123237024
94093123237024
94093123239904
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-6-bb929bfaec24> in <module>
     13 ext_x2 = func2(ext_x)
     14 print(id(ext_x2))
---> 15 assert ext_x is ext_x2, "the objects are not the same"

AssertionError: the objects are not the same
```

This doesn't work. Why? Let's take it apart using another tool in the python standard library, the `dis` module.

## Disassembling our snippets

```python
import dis
print("Disassembling the first snippet")
dis.dis("""
def func():
    x = 10
    print(id(10))
    return x

external_x = func()
print(id(external_x))

def func2(inp):
    print(id(inp))
    return inp

external_inp = func2(external_x)
print(id(external_inp))
assert external_x is external_inp, "The item is not the same. This assertion should not have been raised"
""")
###
print("Disassembling the failing snippet")
dis.dis("""
def func():
    x = 10
    print(id(x))
    return x

ext_x = func()
print(id(ext_x))

def func2(inp):
    inp = inp**2
    return inp

ext_x2 = func2(ext_x)
print(id(ext_x2))
assert ext_x is ext_x2, "the objects are not the same"
""")

```

When you run this file, you should see the following output. Do not be too intimidated by how long it seems, it is fairly easy to understand once you know how to read it.

[The official python documentation on the `dis` library is excellent and you should try to go through that before you read ahead](https://docs.python.org/3/library/dis.html)


```
Disassembling the first snippet
  2           0 LOAD_CONST               0 (<code object func at 0x7f000e812030, file "<dis>", line 2>)
              2 LOAD_CONST               1 ('func')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (func)

  7           8 LOAD_NAME                0 (func)
             10 CALL_FUNCTION            0
             12 STORE_NAME               1 (external_x)

  8          14 LOAD_NAME                2 (print)
             16 LOAD_NAME                3 (id)
             18 LOAD_NAME                1 (external_x)
             20 CALL_FUNCTION            1
             22 CALL_FUNCTION            1
             24 POP_TOP

 10          26 LOAD_CONST               2 (<code object func2 at 0x7f000e81c390, file "<dis>", line 10>)
             28 LOAD_CONST               3 ('func2')
             30 MAKE_FUNCTION            0
             32 STORE_NAME               4 (func2)

 14          34 LOAD_NAME                4 (func2)
             36 LOAD_NAME                1 (external_x)
             38 CALL_FUNCTION            1
             40 STORE_NAME               5 (external_inp)

 15          42 LOAD_NAME                2 (print)
             44 LOAD_NAME                3 (id)
             46 LOAD_NAME                5 (external_inp)
             48 CALL_FUNCTION            1
             50 CALL_FUNCTION            1
             52 POP_TOP

 16          54 LOAD_NAME                1 (external_x)
             56 LOAD_NAME                5 (external_inp)
             58 COMPARE_OP               8 (is)
             60 POP_JUMP_IF_TRUE        70
             62 LOAD_GLOBAL              6 (AssertionError)
             64 LOAD_CONST               4 ('The item is not the same. This assertion should not have been raised')
             66 CALL_FUNCTION            1
             68 RAISE_VARARGS            1
        >>   70 LOAD_CONST               5 (None)
             72 RETURN_VALUE

Disassembly of <code object func at 0x7f000e812030, file "<dis>", line 2>:
  3           0 LOAD_CONST               1 (10)
              2 STORE_FAST               0 (x)

  4           4 LOAD_GLOBAL              0 (print)
              6 LOAD_GLOBAL              1 (id)
              8 LOAD_CONST               1 (10)
             10 CALL_FUNCTION            1
             12 CALL_FUNCTION            1
             14 POP_TOP

  5          16 LOAD_FAST                0 (x)
             18 RETURN_VALUE

Disassembly of <code object func2 at 0x7f000e81c390, file "<dis>", line 10>:
 11           0 LOAD_GLOBAL              0 (print)
              2 LOAD_GLOBAL              1 (id)
              4 LOAD_FAST                0 (inp)
              6 CALL_FUNCTION            1
              8 CALL_FUNCTION            1
             10 POP_TOP

 12          12 LOAD_FAST                0 (inp)
             14 RETURN_VALUE
Disassembling the failing snippet
  2           0 LOAD_CONST               0 (<code object func at 0x7f000e812030, file "<dis>", line 2>)
              2 LOAD_CONST               1 ('func')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (func)

  7           8 LOAD_NAME                0 (func)
             10 CALL_FUNCTION            0
             12 STORE_NAME               1 (ext_x)

  8          14 LOAD_NAME                2 (print)
             16 LOAD_NAME                3 (id)
             18 LOAD_NAME                1 (ext_x)
             20 CALL_FUNCTION            1
             22 CALL_FUNCTION            1
             24 POP_TOP

 10          26 LOAD_CONST               2 (<code object func2 at 0x7f000e81c4b0, file "<dis>", line 10>)
             28 LOAD_CONST               3 ('func2')
             30 MAKE_FUNCTION            0
             32 STORE_NAME               4 (func2)

 14          34 LOAD_NAME                4 (func2)
             36 LOAD_NAME                1 (ext_x)
             38 CALL_FUNCTION            1
             40 STORE_NAME               5 (ext_x2)

 15          42 LOAD_NAME                2 (print)
             44 LOAD_NAME                3 (id)
             46 LOAD_NAME                5 (ext_x2)
             48 CALL_FUNCTION            1
             50 CALL_FUNCTION            1
             52 POP_TOP

 16          54 LOAD_NAME                1 (ext_x)
             56 LOAD_NAME                5 (ext_x2)
             58 COMPARE_OP               8 (is)
             60 POP_JUMP_IF_TRUE        70
             62 LOAD_GLOBAL              6 (AssertionError)
             64 LOAD_CONST               4 ('the objects are not the same')
             66 CALL_FUNCTION            1
             68 RAISE_VARARGS            1
        >>   70 LOAD_CONST               5 (None)
             72 RETURN_VALUE

Disassembly of <code object func at 0x7f000e812030, file "<dis>", line 2>:
  3           0 LOAD_CONST               1 (10)
              2 STORE_FAST               0 (x)

  4           4 LOAD_GLOBAL              0 (print)
              6 LOAD_GLOBAL              1 (id)
              8 LOAD_FAST                0 (x)
             10 CALL_FUNCTION            1
             12 CALL_FUNCTION            1
             14 POP_TOP

  5          16 LOAD_FAST                0 (x)
             18 RETURN_VALUE

Disassembly of <code object func2 at 0x7f000e81c4b0, file "<dis>", line 10>:
 11           0 LOAD_FAST                0 (inp)
              2 LOAD_CONST               1 (2)
              4 BINARY_POWER
              6 STORE_FAST               0 (inp)

 12           8 LOAD_FAST                0 (inp)
             10 RETURN_VALUE 
```

Look at the first half, which says "disassembling the first snippet".


## Let's return a dictionary instead!

## Nested Functions - Finally

## Overdrive: Nested classes

## Bonus Bonus: Returning Static Methods

## We Get the Idea: So what?

## `__closure__` and what it means

## End Note

## A Personal Story

The conversation at the beginning of this article came about because I had just come out of an interview where the interviewer asked me to explain Python closures.
I had faltered, not because I didn't know, but because, oddly enough, I thought there was nothing special about how you can essentially play ping pong with objects
in Python. Most languages do this. Python does this only because C does it. You can return pointers, can't you?

All in all, a confusing interview let me to understand something in depth, and helped me learn.


