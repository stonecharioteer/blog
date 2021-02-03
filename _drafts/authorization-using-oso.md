---
layout:    "post"
title:     "Authorization in Python using `oso`"
categories: ['learning']
---

Auth is one of the more underrated features in software. Not only is it hard
to do in a secure manner, it is also seldom appreciated when it is done well.
When auth works, it's business as usual, and when it doesn't, someone messed
up.

When people say auth, they could mean one of two things: *authentication*, or,
*authorization*.

*Authentication* deals with user identity. Is user `abc` who they say they are?
It deals with user IDs and passwords and validation. It could additionally
deal with user tokens, sessions, and cookies among other things.

*Authorization* deals with a user's permissions. Is user `abc` *allowed* to
do the thing they have requested? Where are the authorization rules?
Who is allowed to use this portion of your application? Who is denied it?

This article deals with *authorization* and not authentication.

When a developer goes about looking for a way to configure authorization, they
usually arrive at *roles*. A user's *role* is assigned certain permissions,
and if you need your user to be able to do something, then just add him
to that role. Easy-peasy.

There is a problem with this approach. The roles have to be checked in your
code, time and again? Want to add a new feature only admins with `cat` in
their username can perform on every third Sunday? Tough luck, you can't do that.

Or maybe you can.

## What is `oso`?

`oso` is a library that takes care of authorization. In coding terms, `oso`
allows you to take code that looks like this:

```python
def user_can_do_this(user):
    if user.is_admin and user.id in ["abc","xyz", "lkjh"]:
        return True
    else:
        return False


if user_can_do_this(user):
    print("I can do this!")
else:
    print("Access denied!")
```

And rewrite it like this:

```python

if oso.is_allowed(user, "can_do", this):
    print("I can do this!")
else:
    print("Access denied!")
```

And in your rules:

```
allow(user, "can_do", this) if user.is_admin and user.id in ["abc","xyz", "lkjh"]
```

For now, ignore what is inside the `allow` line. Indeed, also ignore the *words*
`user`, `"can_do"` and `this`. *None of them have any meaning beyond what you
assign it in your code*.


While this doesn't look like much, it actually is. `oso` provides users
the `polar` declarative language with which to declare *policies* for the
application.

These policies enable developers to abstract the actual rules of authorization
and instead focus on their code. Everything else is denied to the user.

Yes, `oso` is *deny by default*. No one gets to do anything if you haven't
defined a rule that you're attempting to use.

## Why do I need `oso`?

If you're used to doing things with `if` statements, or perhaps modular
`decorators`, and that's a good pattern to have, why would you need `oso`?

1. `oso` does modularization for you.
2. You can use the Polar language syntax to define rules in a simple way.
3. You can hot load policies on the fly, meaning you can come up with runtime
   policies that you couldn't do without considerable effort.
4. `oso` also gives you plugins for your favourite languages: You can reuse
   your policies *across* your organization, in multiple languages.
5. You can separately version control your policies.
6. Policies are just strings. You can store them in a database, if you want you. Also, [/r/madlads](https://reddit.com/r/madlads) is :point_right: that way.

## Hello `oso`

So how do you use `oso` in your python code?


First, install the library.

```bash
pip install oso
```

Then, create a new python file.

```python

from oso import Oso

oso_object = Oso()

oso_object.load_str("""allow("user", "can_use", "this_program");""")

if oso_object.is_allowed("user", "can_use", "this_program"):
    print("Hello from oso")
else:
    print("Access denied")
```

All examples from this post are available [here as a Github repository.](https://github.com/stonecharioteer/oso-examples)

### What's Going On?

The `oso` documentation begins users with showing how you can integrate `oso` into a web application written in native Python. However, I believe in a first principles approach.

In this example, we're loading the `oso` library, and then immediately creating an instance of the `oso.Oso` class. This enables us to then bind *policies* to the object.

An `oso` policy is declared in a language known as Polar. Polar takes inspiration from Prolog, and I like to think of its rule system as a paradigm you'd find in Rust's pattern matching. Don't let any of this intimidate you: I'll get to it later. For now, all you need to know is that we've added `allow("user", "can_use", "this_program");` to the policies in the `oso_object` object.

Note that I've used triple double quotes because Polar uses only double quotes for its strings.

This line essentially says: "If `allow` is triggered with 3 variables equal to, *literally*: `"user"`, `"can_use"` and `"this_program"`, then evaluate to `true`. (Polar uses `true`/`false` as synonyms for Python's `True`/`False`).

Next, we use this policy in our script, with `oso_object.is_allowed`. Note that the arguments to `is_allowed` are *exactly* the same as those to `allow`.

`oso`'s `is_allowed` looks for a function called `allow` loaded into the object which has a matching pattern. Again, don't worry too much about this for now. And it finds the single policy we have defined and realizes that the policy matches and evaluates to `True` (this is on the Python side).

Hence, the line `print("Hello from oso")` works.

### What Happened?

Under the hood, `oso` evaluates Polar rules and loads them into the `oso.Oso` object that we create. Those rules dictate the outcome of `oso_object.is_allowed` calls. But here's a question for you:

Where are the rules coming from?

Polar is a declarative language. While it supports things like integers and some rudimentary math, strings and boolean values, it doesn't have much else.

So what is `allow`?

The interesting thing about `oso` and its choice with Polar is that `allow` is whatever you want it to be.

Let me reiterate.

```polar
allow("user", "can_use", "this_program");
```

This *defines* a policy called `allow` with those exact parameters.

`is_allowed` matches its arguments with this policy, and realizes that it matches the rule, thus evaluating to `True`.

### What if I want to *deny* access?

That's simple. Just try to call `is_allowed` with anything else.

In our previous file, add the following:


```python
if oso_object.is_allowed("user-123", "can_run", "this_program"):
    print("Hello again, but you probably can't run this line.")
else:
    print("You weren't authorized by the rules!")
```

This `is_allowed` will evaluate to `False`, since it doesn't match the rule
that we've loaded into the`oso_object`.

Remember what I've been saying about *pattern-matching*? Well, Oso looks for
an exact match for the rules. You *could* generalize it further by using types,
or your own classes, but we'll get to that later.

For now, you need to just understand that `oso` essentially does a 1:1 match
with the rules in your `oso_object` and evaluates `is_allowed` based on a
suitable `allow` policy.

## `oso` in a CLI

<!-- TODO: explain how to use `oso` with argparse, suggest usage with `click` -->
<!-- TODO: Use `pandas` and show how to limit the use of something when the dataframe is too large.  -->
## Where's the Server?

An easy misconception is that `oso` needs to be used with an API. It doesn't.
In fact, you could use `oso` for regular applications or scripts. If you
want to dictate whether your code can or cannot do something, go right ahead
and use `oso`. You could recreate `rm` should you want to, integrating checks
for whether a user to allowed to delete a file or not. You could also forget
about even having a `user`, you could instead use `oso` to decide whether or
not a particular step happens in your code. I could see this being used for
an IoT project, decided to check if your house is too hot or too cold. Perhaps
this rule could then be used in multiple places, from turning up the thermostat
to turning on the Air Conditioner, or ordering soup online, or getting icecream.

Honestly, the sky is the limit with this.

However, one place where authorization is definitely needed is in a web app.
That's where `oso` was designed to be used, despite my proclivity to use it
in hacked-up scripts.

## `oso` and `Flask`

<!-- TODO: Explain how to use `oso` in a Flask app. -->

### With `Flask-Login`

### With `flask_jwt_extended`

## Advanced Patterns

## Getting Help
