
:blogpost: true
:date: June 29, 2022
:category: Tech
:tags: Rust


.. _rust-reqwest-headers:

==================================================
Adding HTTP Headers to a HTTP Reqwest with Rust
==================================================

How do you add a header to a HTTP Request in Rust?

I got stuck for lack of documentation when adding an `X-API-KEY` header to a
HTTP request that I'm performing using Rust. In this article I discuss what I
needed to do.

As always, I'm going to use Python and Flask to write the test server.
