:blogpost: true
:date: March 13, 2022
:category: Tech
:tags: Learning, Teaching, Programming

======================================
Learning a New Programming Language
======================================

How do you learn a new programming language? I find myself constantly wanting to
learn a few new languages, and I've failed several times over. Sometimes I
wonder how I learnt Python, and remember that I didn't really focus on getting
things right. I just dove into the problem after reading an introductory book,
and it worked for me. However, that approach works *only* for blank slates. Back
then I didn't know what a package manager was, I didn't care whether I was
polluting the environment with global dependencies, and I was definitely not
concerned about CICD. Today, I am very concerned about all of that. Indeed,
these are merely the tip of the iceberg when it comes to the problems I've been
facing.

This made me wonder what works. I believe that there should be a sort of Coding
Katas to learn a new programming language. It should help you achieve what you
*should* be able to do after learning one.

-------------------------------------
Hello World CLI
-------------------------------------

Write a Command Line Interface that implements Hello World as one of its
subcommands. The base command should do nothing for now, and it should output
help if it doesn't recieve any subcommand. Support the following:

```bash
tool --help
tool hello --help
tool hello <token:optional:default=world>
```
Use built-ins to do this, unless the language doesn't support CLI parsing. If it
doesn't, find the most popular, and well-documented CLI library and use that.

For the output, make sure it capitalizes the first letter of the token. The
token *can* be more than one word, and it should also accept tokens through the
unix ``|``.

```bash
echo 'Vinay' | hello
```

-------------
FizzBuzz CLI
-------------

Extend your ``tool`` CLI to support subcommands. Build a similar CLI that
outputs FizzBuzz. The now *required* token will take a number. The number *must*
be a positive integer.

```bash
tool fizzbuzz --help
tool fizzbuzz <token:required:positive-integer>
```

--------------
Testing
--------------

Write tests for both these commands. Ensure that the CLI itself is also tested.
Look into how to use hooks/wrappers for STDIN, STDOUT and STDERR and test that
the designed output is actually printed.

-----------------
To Do CLI
-----------------

Build a new CLI subcommand for ``tool`` that implements ``todo``. This should
do the following.

1. Use a ``csv`` file as its database. This file should be stored in a
   configurable location, by default in ``~/.tool/default.todo.csv``.
2. Support ``~/.config/tool.toml`` for a configuration file. If a
   ``todo.toml`` file exists in the current directory, read from that and
   override the defaults.
3. Support ``TOOL_CONFIG_FILE`` environment variable that points to a file.
   Support both relative and absolute file paths.
4. If any of the default and expected files don't exist, create them with ``tool
   todo init``, which should be the first command you run.
5. Support ``tool todo list`` which should print out the pending todo items in a
   colorful format. Implement ``--format csv|json|pretty``,
   of which ``pretty`` is the default, showing colors and UTF-8 symbols.
   Implement ``--no-color`` and ``--no-emojis``.
6. Try to detect if the terminal can show emojis and other symbols or not.
7. Implement ``tool todo add``, ``tool todo update`` and ``tool todo cancel``.
8. Implement ``tool todo archive``, which will move all the older items into an
   ``archive.csv`` file.
9. Implement labels, category, project, assignee, date, start-work, end-work,
   start-date, end-date. Ensure any enumeration exists in the config file and
   not in the code.
10. Finally, allow the user to choose whether to write to a sqllite3 file or to
    a csv, use sqllite by default.

-------------------------------
TUI Application
-------------------------------

Build a TUI interface for the TODO application.

--------------------------------
HTTP API
--------------------------------
