:blogpost: true
:date: Jan 24, 2022
:category: Learning
:tag: til, python, ds

============================================
Creating Fixed Length Iterables in Python
============================================


If you want to create an iterable of a fixed length in python, use
``collections.deque`` with the ``maxlen`` parameter.

.. code-block:: python
   :linenos:

   import collections

   fixed_list = collections.deque(5*[None], 10)

   # this is now a fixed list of items 10.
   # by _appending_ more items, you'd be dropping items
   # from the beginning.

   fixed_list.append(1)
   print(fixed_list)

Note that this merely calls ``appendleft``.
