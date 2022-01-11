.. _notes-leetcode:
=========================
Leetcode
=========================

.. note::
   This section of my notes is directed towards interview prep and leetcode
   practice.  I'll host solutions and problems that I've worked on here, so
   that I can keep track of my preparation.

   All problems are the property of Leetcode and the rights thereof belong to
   them.
.. {{{ Adding New Solutions

---------------------
Adding New Solutions
---------------------

Add an item to ``problems.toml`` and run ``create_solutions.py``. Do not manually
create solution files.

A problem item in the ``toml`` file is defined as:

.. code-block:: toml

   [[problems.leetcode]]
   name = "2-Sum-Problem"
   url = "https://leetcode.com/problems/two-sum/"
   number = 1
   level = "EASY"
   labels = [ "striver", "striver-4",]

.. }}}

.. {{{ Striver List
---------------
Striver List
---------------

This is a rough timeline of problems that follow the `Striver SDE Sheet.
<https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/>`_
Note that for now, I'm sticking only to the Leetcode problems linked therein, since I
have setup a testing pipeline targetting Leetcode only.


.. panels::
   :container: timeline
   :column: col-6 p-0
   :card:

   ---
   :column: +entry left

   **Day 1**
   ^^^

   .. toctree::

      lc_0073
      lc_0118
      lc_0031
      lc_0053
      lc_0075
      lc_0012


   ---
   :column: +right
   ---
   :column: +left

   ---
   :column: +entry right

   **Day 2**
   ^^^

   .. toctree::

      lc_0048
      lc_0056
      lc_0088
      lc_0287


   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 3**
   ^^^

   .. toctree::

      lc_0074
      lc_0050
      lc_0169
      lc_0229
      lc_0062
      lc_0493

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 4**
   ^^^

   .. toctree::

      lc_0018
      lc_0128
      lc_0001
      lc_0003


   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 5**
   ^^^

   .. toctree::

      lc_0206
      lc_0876
      lc_0021
      lc_0019
      lc_0002
      lc_0237

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 6**
   ^^^

   .. toctree::

      lc_0160
      lc_0141
      lc_0025
      lc_0234
      lc_0142
      lc_0061

   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 7**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 8**
   ^^^

   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 9**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 10**
   ^^^
   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 11**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 12**
   ^^^
   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 13**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 14**
   ^^^
   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 15**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 16**
   ^^^
   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 17**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 18**
   ^^^
   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 19**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 20**
   ^^^
   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 21**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 22**
   ^^^
   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 23**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 24**
   ^^^
   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 25**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 26**
   ^^^
   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 27**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 28**
   ^^^
   ---
   :column: +left
   ---
   :column: +right
   ---
   :column: +entry left

   **Day 29**
   ^^^

   ---
   :column: +right
   ---
   :column: +left
   ---
   :column: +entry right

   **Day 30**
   ^^^
.. }}}

.. todo::

   Add general index since I'll also be solving problems that are not in the
   categorized lists.

   Perhaps I should just move each of these labelled things to their own
   toctrees. Panels are overkill if I use them for everything
