:blogpost: true
:date: June 25, 2022
:category: Tech
:tags: Rust

.. _rust-reqwest-retry:

=====================================
Retrying a HTTP Reqwest with Rust
=====================================

How do you retry an HTTP request in Rust?

I have been using Rust as my only programming language for a few months now at
Merkle Science. One of the things I have been building lately has been a crawler
that looks through a paginated API for responses.

.. note::

   If you're building something like this and shipping a single light-weight
   binary isn't your requirement, I'd recommend doing this in Python and using
   the ``tenacity`` package for retrying queries.

When building one of these, you will definitely need something that incorporates
a "retry when you fail" mechanism because repeated API calls, or *any* API calls
for that matter, are bound to fail. You might have a rate limited API, or you
might just have an unreliable network.

I had both these problems and needed to build something that could repeatedly
try to make a GET request.

I was using the ``reqwest`` crate to make these requests and I kept getting
a ``reqwest::Error``. Oddly enough, I was getting this both when the network
failed, or when the payload didn't have the expected schema.


To understand this, let's first put together a simple server that will mimic
unreliable behaviour.

For simplicity, I'm going to write this in Flask.

.. code-block:: python
   :linenos:

   import flask
   import random

   app = flask.Flask(__name__)

   @app.route("/<int:which>")
   def index(which):
      if random.random() > 0.5:
         return {}, 404
      if which == 1 and random.random() > 0.3:
         return {
            "name": "John Doe",
            "age": 28
         }
      else:
         return {
            "uuid": "40fc1511-00ed-4021-9733-41a3ccbcf441",
            "packet_size": 523
         }


Save the above code snippet into a file named ``app.py``.

To run this, create a virtual environment using Python: ``python3 -m venv env``,
activate it: ``source ./env/bin/activate``, and install Flask: ``python3 -m pip
install flask``. Then, run the following ``FLASK_DEBUG=true flask run``

While you don't need to understand how this works, all you need to know is that
this now provides a simple, *unreliable* webserver that has only 2 routes:
``http://127.0.0.1:5000/1`` and ``http://127.0.0.1:5000/2``.

Both these routes have a 51% chance of returning a 404, and the first URL has an
added 71% chance of returning the wrong response.


.. note::

   The term *"wrong"* is subjective, and for the sake of an example, I'm going
   to pretend that all APIs in the world always return the agreed-upon payload
   for a given route. Such a world doesn't exist though.

To get this response, I wrote the following code.

.. note::

   To get the following code running make sure you add the following lines to
   your ``Cargo.toml`` file's ``[dependencies]`` section.

   .. code-block:: toml

      env_logger = "0.9.0"
      log = "0.4.17"
      reqwest = { version = "0.11.11", features = ["blocking", "serde_json", "json"] }
      serde = { version = "1.0.137", features = ["derive"] }
      serde_json = "1.0.81"
      tokio = { version = "1.19.2", features = ["full", "rt"] }

You will need to setup Rust before you try to run this code.

.. code-block:: rust
   :linenos:

   use std::{fmt::Debug, time::Duration};
   use serde::{Serialize, Deserialize};

   #[derive(Debug, Serialize, Deserialize)]
   struct ResponseOne {
      name: String,
      age: u8
   }

   #[derive(Debug, Serialize, Deserialize)]
   struct ResponseTwo {
      uuid: String,
      packet_size: u16
   }

   fn main() {
      let url_1 = "http://127.0.0.1:5000/1".to_string();
      let resp_1: ResponseOne = reqwest::blocking::get(url_1).unwrap().json().unwrap();
      log::info!("resp_1 = {resp_1:?}");
   }


Running this with ``RUST_LOG=info cargo run`` fails in one of two ways.

First, if the server is running, this fails because the payload is not as
expected.

.. code-block::

   thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: reqwest::Error { kind: Decode, source: Error("missing field `name`", line: 1, column: 2) }', src/main.rs:50:77
   note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Next, if you kill the flask server, you will get the following response.

.. code-block::

   thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: reqwest::Error { kind: Request, url: Url { scheme: "http", cannot_be_a_base: false, username: "", password: None, host: Some(Ipv4(127.0.0.1)), port: Some(5000), path: "/1", query: None, fragment: None }, source: hyper::Error(Connect, ConnectError("tcp connect error", Os { code: 111, kind: ConnectionRefused, message: "Connection refused" })) }', src/main.rs:50:61
   note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Both of these are standard errors you will encounter when building a crawler.
And the answer to both of these is: "just try again". Rust's error handling
isn't exactly error handling, so you cannot just bypass an error and try again
for a fixed number of times without being extremely verbose about it. One way to
handle this is to find a crate that does the job for you.

There were several, but only the `again crate <https://crates.io/crates/again>`_
really worked the way I needed it to. I had several requirements.

1. I need to be able to retry a query.
2. I need to be able to wait and retry after some time.
3. I should be able to introduce some randomness between calls, aka *jitter*, so
   that the API doesn't realize it's being spammed with programmed calls.
4. I should stop after a reasonable amount of time because I am not a spammer.

The again crate works for all of these, with one slight caveat. The
``again::retry`` function, and all of its variants, call *async* functions, not
synchronous ones. In more specific terms, calls that ``again::retry`` makes need
to return a ``Future`` object, one that can be waited upon by the ``again``
crate itself. So the ``reqwuest::blocking`` calls are out of the question.

Thankfully, reqwest by default uses async calls. However, Rust's ``main``
function is a synchronous one, and cannot ``await`` on an async call out of the
box.

``tokio`` to the rescue!

``tokio`` comes with a runtime feature that allows us to block upon an async
call within a non-async function. I won't dive too much into that right now, but
that rabbit hole led down to this code.

.. code-block:: rust
   :linenos:

   /// Get a specific typed response
   async fn get_typed_payload<T>(url: &String) -> Result<T, reqwest::Error> where for<'de> T: serde::Deserialize<'de> {
      Ok(reqwest::get(url).await?.json().await?)
   }

   fn main() {
      env_logger::init();
      let rt = tokio::runtime::Runtime::new().unwrap();
      let retry_policy = again::RetryPolicy::exponential(Duration::from_secs(1))
         .with_jitter(true)
         .with_max_delay(Duration::from_secs(3))
         .with_max_retries(10);
      let url_1 = "http://127.0.0.1:5000/1".to_string();
      let resp_1 = rt.block_on({
               let response = retry_policy.retry(|| {
                  get_typed_payload::<ResponseOne>(&url_1)
               });
         response
      }).unwrap();
      log::info!("Response 1: {resp_1:?}");
      let url_2 = "http://127.0.0.1:5000/2".to_string();
      let resp_2 = rt.block_on({
               let response = retry_policy.retry(|| {
                  get_typed_payload::<ResponseTwo>(&url_2)
               });
         response
      }).unwrap();
      log::info!("Response 2: {resp_2:?}");
   }

This above code can be run with ``RUST_LOG=info,again=trace cargo run`` and will
repeatedly try the API until it gets a response. The ``retry_policy`` sets a
starting duration of 1 second, increases it until it reaches 3 seconds, and
tries at most 10 times before actually giving up on the URL.

The ``get_typed_payload`` function is written so as to abstract away the JSON
payload extraction, and because the ``retry`` function needs an async function
that returns a result with a very clear Error type. Thankfully reqwest returns
only one possible error type.

Some things I learnt about Rust when writing this was about generics and
lifetimes.

The ``for<'de> T: serde::Deserialize<'de>`` bit denotes that the
``get_typed_payload`` function can adapt to return any type that implements
``serde::Deserialize``. And because the value that it returns *should* live for
the lifetime of the variable it is passed, which in this case is the ``url``,
you need to denote that as well with the ``for <'de>`` bit. One thing that this
also results in is that the actual ``url`` object should be created outside of
both the ``retry`` block and the ``block_on`` block, so that it lives beyond
those confines.

This was a fun little exercise of doing something I've done a hundred times or
more in Python in Rust. I'm continuing my journey merely because this way I
learn how to do things that I've taken for granted in a language like Python,
and I'm learning about Rust along the way.

.. note::

   If you enjoy coding in Rust, or are interested enough to learn, and are
   interested in engineering problems in general, I'm hiring. Hit me up on
   Twitter or LinkedIn for a role at Merkle Science. Alternately, send us an
   email at `careers@merklescience.com`_
