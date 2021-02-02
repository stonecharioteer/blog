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

## Hello `oso`
