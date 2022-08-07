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

.. toctree::
   :caption: Leetcode Problems

   lc_0001.rst
   lc_0002.rst
   lc_0003.rst
   lc_0018.rst
   lc_0019.rst
   lc_0021.rst
   lc_0025.rst
   lc_0031.rst
   lc_0048.rst
   lc_0050.rst
   lc_0053.rst
   lc_0056.rst
   lc_0061.rst
   lc_0062.rst
   lc_0073.rst
   lc_0074.rst
   lc_0075.rst
   lc_0088.rst
   lc_0118.rst
   lc_0121.rst
   lc_0128.rst
   lc_0136.rst
   lc_0141.rst
   lc_0142.rst
   lc_0160.rst
   lc_0169.rst
   lc_0206.rst
   lc_0217.rst
   lc_0229.rst
   lc_0234.rst
   lc_0237.rst
   lc_0238.rst
   lc_0268.rst
   lc_0287.rst
   lc_0442.rst
   lc_0493.rst
   lc_0876.rst
   lc_2022.rst

.. {{{ using the json dataset with ``jq``

----------------------------------------
Using the Leetcode Dataset with ``jq``
----------------------------------------

.. note::
   Make sure you install `jq, <https://stedolan.github.io/jq/>`_ the CLI tool to
   filter and use JSONs for this section.

I've collected all the leetcode questions and metadata into a json which is
placed `in the github repo for my blog.
<https://github.com/stonecharioteer/blog/raw/master/notes/leetcode/data_sorted.json>`_
I want to do more with it, but until I do, you should use ``jq`` to filter and
look through it.

I'll document some commands here.

Getting Questions by Company
--------------------------------

.. code-block:: bash

   jq '.[] | select(.companyTagStats | strings | ascii_downcase | test("COMPANY_NAME_LOWERCASE") | {id:
   .questionId, category: categoryTitle, difficulty, url,
   title, tags: [.topicTags[].slug]}' data_sorted.json

.. warning::

   This query will change, since right now, I'm storing ``companyTagStats`` in
   its raw text form for now. I want to convert it to a list, but I don't have
   time.

Getting Questions by Tags
-------------------------------

.. code-block:: bash

   jq '.[] | {id: .questionId, title, url, category: .categoryTitle, difficulty,
   tags: [.topicTags[].slug]} | select(.tags[] | ascii_downcase | contains("TAG_NAME_LOWERCASE"))' data_sorted.json


Getting Questions by Category
-------------------------------

.. code-block:: bash

   jq '.[] | {id: .questionId, title, url, category: .categoryTitle, difficulty,
   tags: [.topicTags[].slug]} | select((.category | ascii_downcase) == "CATEGORY_LOWERCASE")' data_sorted.json

.. }}}

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
