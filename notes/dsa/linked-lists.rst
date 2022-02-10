.. notes-dsa-linked-list:
================================
Linked Lists
================================

I'll be documenting implementations and operations using a linked list here.

-----------------------------
Resources
-----------------------------

Here are some resources I've found useful when learning about linked lists:

1. `freeCodeCamp.org's Video <https://www.youtube.com/watch?v=Hj_rA0dhr2I>`_


.. {{{ Definition of a node
-----------------------------
Definition of a Node
-----------------------------

.. tabs::

   .. group-tab:: Python

      .. literalinclude:: /code/dsa/linked_lists/python/definition.py
         :language: python
         :linenos:

   .. group-tab:: Javascript

      .. literalinclude:: /code/dsa/linked_lists/javascript/definition.js
         :language: javascript
         :linenos:

.. }}}
.. {{{ Creating a Linked List
-----------------------
Creating a Linked List
-----------------------

.. tabs::

   .. group-tab:: Python

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/python/creation_iterative.py
               :language: python
               :linenos:

         .. group-tab:: Recursive

            .. code-block:: python

               print("hello, world")


   .. group-tab:: Javascript

      .. tabs::

         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/javascript/creation_iterative.js
               :language: javascript
               :linenos:

         .. group-tab:: Iterative

            .. code-block:: javascript

               console.log("Hello, world!")

.. }}}
.. {{{ Printing Each Item of a Linked List
----------------------------------------
Printing Each Item of a Linked List
----------------------------------------

.. tabs::

   .. group-tab:: Python

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/python/printing_iterative.py
               :language: python
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/python/printing_recursive.py
               :language: python
               :linenos:


   .. group-tab:: Javascript

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/javascript/printing_iterative.js
               :language: javascript
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/javascript/printing_recursive.js
               :language: javascript
               :linenos:

.. }}}
.. {{{ Summing a Linked List
----------------------------------
Summing a Linked List
----------------------------------
.. tabs::

   .. group-tab:: Python

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/python/sum_list_iterative.py
               :language: python
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/python/sum_list_recursive.py
               :language: python
               :linenos:


   .. group-tab:: Javascript

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/javascript/sum_list_iterative.js
               :language: javascript
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/javascript/sum_list_recursive.js
               :language: javascript
               :linenos:

.. }}}
.. {{{ Finding a value in a linked list
-------------------------------------
Finding a Value in a Linked List
-------------------------------------
.. tabs::

   .. group-tab:: Python

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/python/find_iterative.py
               :language: python
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/python/find_recursive.py
               :language: python
               :linenos:


   .. group-tab:: Javascript

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/javascript/find_iterative.js
               :language: javascript
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/javascript/find_recursive.js
               :language: javascript
               :linenos:

.. }}}
.. {{{ Get Node Value
----------------------------
Get Node value at Index
----------------------------
.. tabs::

   .. group-tab:: Python

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/python/get_node_value_iterative.py
               :language: python
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/python/get_node_value_recursive.py
               :language: python
               :linenos:


   .. group-tab:: Javascript

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/javascript/get_node_value_iterative.js
               :language: javascript
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/javascript/get_node_value_recursive.js
               :language: javascript
               :linenos:

.. }}}
.. {{{ Reverse Linked List
--------------------
Reverse Linked List
--------------------
.. tabs::

   .. group-tab:: Python

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/python/reverse_iterative.py
               :language: python
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/python/reverse_recursive.py
               :language: python
               :linenos:


   .. group-tab:: Javascript

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/javascript/reverse_iterative.js
               :language: javascript
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/javascript/reverse_recursive.js
               :language: javascript
               :linenos:
.. }}}
.. {{{ Zipping Two Linked Lists
---------------------------
Zipping Two Linked Lists
---------------------------
.. tabs::

   .. group-tab:: Python

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/python/zip_iterative.py
               :language: python
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/python/zip_recursive.py
               :language: python
               :linenos:


   .. group-tab:: Javascript

      .. tabs::

         .. group-tab:: Iterative

            .. literalinclude:: /code/dsa/linked_lists/javascript/zip_iterative.js
               :language: javascript
               :linenos:


         .. group-tab:: Recursive

            .. literalinclude:: /code/dsa/linked_lists/javascript/zip_recursive.js
               :language: javascript
               :linenos:

.. }}}

.. {{{ Design of a Linked List (LC)
--------------------
Linked List Design
--------------------

This is an implementation of a Linked List to satisfy the `Leetcode Linked List
card. <https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/>`_

.. tip::

   This has a few adjustments I made because of how the tests are structured on LeetCode,
   but I wouldn't do this exactly this way. For instance ``node = MyLinkedList()`` is meaningless
   since it references a node without a value. I think this was done only to allow deleting the head
   node of a single-value linked list that would now become an empty linked list.

.. literalinclude:: /code/dsa/linked_lists/python/design.py
   :language: python
   :linenos:

.. }}}
