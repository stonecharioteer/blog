.. notes-dsa-graphs:
==========================
Graphs
==========================

------------
Resources
------------

1. `freeCodeCamp.org <https://www.youtube.com/watch?v=tWVWeAqZ0WU>`_
2. `Red Blob Games - Grids and Graphs <https://www.redblobgames.com/pathfinding/grids/graphs.html>`_
3. `Red Blob Games - Introduction to the A* Algorithm <https://www.redblobgames.com/pathfinding/a-star/introduction.html>`_

.. {{{ Glossary
---------------
Terminology
---------------

Graphs
==========

A graph is a way of describing the relationship between things. Graphs don't really have to represent a way to get to
a place. That's a kind of graph, but you could have graphs that only just say that something is related to another thing.

Nodes
=========

A node is a unit of data, it could be used to represent anything. In programming terms, it could be an *object*.
Nodes are also called Vertices.

Edges
=========

An edge is a connection between 2 nodes. An edge can be visualized as the relationship between things.


Neighbour Nodes
==================

A Neighboring node is a node that is connected to the current node by an edge.

.. }}}
.. {{{ Types
------------------
Types of Graphs
------------------

Directed Graphs
==================

A directed graph shows the *direction* of the relationship between nodes. You can only travel in the direction
that is shown on the graph.


Undirected Graphs
===================

These are graphs wherein the direction has no importance. So you can travel in any direction and the relationship
is the same.

.. }}}
.. {{{ Representation
-------------------------
Representation of Graphs
-------------------------

An adjacency list (something like a hashmap) is used to repesent a graph. It shows how each node is related to
other nodes.

```json
{
   "a": ["b", "c"],
   "b": ["d"],
   "c": ["e"],
   "d": [],
   "e": ["b"],
   "f": ["d"]
}
```

.. }}}
.. {{{ Traversals
----------------------------
Graph Traversals
----------------------------

Traversal of a graph is a way of moving around in a graph.

.. {{{ Depth First Traversal
Depth First Traversal
======================

.. tip::

   This uses a stack.

.. tabs::

   .. group-tab:: Python

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/graphs/python/depth_first_traversal_iterative.py
               :language: python
               :linenos:

   .. group-tab:: Javascript

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/graphs/javascript/depth_first_traversal_iterative.js
               :language: javascript
               :linenos:

.. }}}
.. }}}
