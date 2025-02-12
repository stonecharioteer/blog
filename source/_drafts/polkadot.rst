:blogpost: true
:category: Computer Science
:tags: polkadot, cryptocurrency, blockchains, whitepaper

==================================
The Polkadot Framework
==================================

.. note::

   This is the first of my posts on reading whitepapers, and coincidentally,
   the first of my posts on cryptocurrencies. I don't know much about
   the first-principles of cryptocurrencies and I'd like to improve that.

`Link to the Whitepaper <>`_

This paper describes the Polkadot framework. In its current state (0.1.0), it is
a draft, and is notated as **Draft 1**.

--------------------
Abstract
--------------------

The abstract talks about how there are issues with extensibility and scalability
with present-day blockchain architectures. Dr. Gavin Wood, the author of this
paper, believes that this is because of two parts of the concensus architecture:
*canonicality* and *validity*. This paper presents the *heterogeneous
multi-chain*, which Dr. Wood believes sets the two apart.

.. note::

   Concensus in a blockchain is the term used to describe the process by which
   different "nodes" come to an agreement regarding the history.

   Canonicality is the state of bringing different histories into the "accepted"
   state. Different blockchains have different terms for it, but think of it as
   having the history committed into the blockchain and verified.

   I'm not sure what *validity* means here.

He proposes doing this through reducing the overall functionality of a framework
to just *security* and *transport*, thus introducing a practical means of core
extensibility.

The paper describes bringing scalability into this system by dividing the two
functions: *"scaling out of its bonded core through the incentivisation of
untrusted public nodes"*

.. todo::

   Explain verification somewhere.
