---
title: Today I Learned
layout: post
categories: [learning]
permalink: /til.html
description: "A list of things I learn every day."
customexcerpt: "A list of things I learn every day."
---

This is a page of things I learn/encounter daily. I am trying to organize these so that I can classify them better.
Some are links to blogs, others to github or to other websites where I learn something interesting every day.
I usually structure this with some helpful description so I can find it later.
To be honest, this is mainly so I can track links in a way that is not reliant on external services.
I plan to build a Telegram bot that manages this page for me.
I can then introduce tagging and search, through the bot, of course.

## 2020-08-06
1. Tool | [Phoronix Test Suite is a bunch of open source hardware benchmarking tools for all platforms](https://www.phoronix-test-suite.com/)

## 2020-08-05

1. Tidbit | You can install more than one kernel into a Linux installation and choose which to boot from in Grub.
2. Tool | [xanmod](https://xanmod.org/) and [liqourix](https://liquorix.net/) are custom kernels for Linux desktops and workstations.
3. Linux Kernel 5.8 has a lot of hardware level optimizations.
4. Tool | [Grub Customizer to customize what the grub menu looks like](https://itsfoss.com/grub-customizer-ubuntu/)
5. Tidbit | [Python's `raise` statement has a `from` clause, to preserve full tracebacks.](https://stackoverflow.com/questions/24752395/python-raise-from-usage)
6. RTFM | [Python `raise` statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)

## 2020-08-02

1. Juju is a tool that helps manage server providers, whether they are GCP, AWS, your own servers or Azure, among others, giving you one way to start, setup and run your servers.
2. Juju's configurations are called charms. These are written in Python.
3. EC2 has a Free tier! I can request a bunch of machines here.

## 2020-08-01
1. Tidbit \| `git log --format="%H" -n 1 | cat` outputs the last commit ID.
2. Tidbit \| `collections.defaultdict` takes a *type* not a value. It will initialize based on the default value for that type.
3. Tidbit \| `nodejs` just uses `process` to get command line arguments.


## 2020-07-30

1. Thread \| [Unix Domain Sockets are "sockets" on a single machine. This is what gunicorn uses. Thread on Unix Sockets vs Networking Sockets](https://serverfault.com/questions/124517/whats-the-difference-between-unix-socket-and-tcp-ip-socket)
2. Article \| [Everything in Linux is a File](https://www.tecmint.com/explanation-of-everything-is-a-file-and-types-of-files-in-linux/#:~:text=If%20you%20are%20new%20to,%2C%20everything%20is%20a%20File%E2%80%9D.&text=That%20is%20in%20fact%20true,is%20considered%20as%20a%20file.)
3. Thread \| [Everything is a File](https://unix.stackexchange.com/a/225542) \| Note: See the `ISSOCK` check.
4. Thread \| [Use `os.stat(path).st_mode.S_ISSOCK` to check if a file is a socket](https://stackoverflow.com/questions/17877296/checking-if-path-is-a-socket-in-python-2-7)
5. Article \| [A TCP Request also has a port on the client]()
6. Thought \| UAT's should not be run in CICDs, it should be done completely external to the setup and bringing up an application.
7. Tool \| [`osquery` is a tool to snoop around a Linux system's OS in an SQL syntax](https://linuxhint.com/install_osquery_ubuntu/)
8. Article \| [Karla Burnett - SSL: It's hard to do right](https://recompilermag.com/issues/issue-1/ssl-its-hard-to-do-right/)
9. Paper \| [Maglev: Google's Custom Load Balancer](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/44824.pdf)
10. Paper \| [MapReduce: Simplified Data Processing on Large Clusters](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/16cb30b4b92fd4989b8619a61752a2387c6dd474.pdf)
11. Paper \| [Google Technical Publications](https://research.google/pubs/)
12. Tool \| [`lwan` - Lightweight Asynchronous Multi-Threaded Event-Based Web-Server](https://lwan.ws/)
13. Article \| [How to Read a Technical Paper](http://www.cs.jhu.edu/~jason/advice/how-to-read-a-paper.html)
14. Paper \| [S. Keshav - How to Read a Paper](http://ccr.sigcomm.org/online/files/p83-keshavA.pdf)
15. Blog \| [The Morning Paper: Blog on Reading a CS Paper Every Week](https://blog.acolyer.org/)
16. RTFM \| [Container Networking](https://docs.docker.com/config/containers/container-networking/)
17. Article \| [Julia Evans: How do HTTP Requests Get Sent to the Right Place?](https://jvns.ca/blog/2016/07/14/whats-sni/)
18. Article \| [Julia Evans: A Few Things I've Learnt about Kubernetes](https://jvns.ca/blog/2017/06/04/learning-about-kubernetes/)
19. Article \| [Julia Evans: A Few Things I've Learnt about Computer Networking](https://jvns.ca/blog/2018/03/05/things-ive-learned-networking/)
20. Blog \| [Kamal Marhubi](http://kamalmarhubi.com)
21. Article \| [Kamal Marhubi - Kubernetes from the Ground Up: What Even is a Kubelet](http://kamalmarhubi.com/blog/2015/08/27/what-even-is-a-kubelet/)
22. Article \| [Kamal Marhubi - Kubernetes from the Ground Up: the API Server](http://kamalmarhubi.com/blog/2015/09/06/kubernetes-from-the-ground-up-the-api-server/)
23. Article \| [Kamal Marhubi - Kubernetes from the Ground Up: The Scheduler](http://kamalmarhubi.com/blog/2015/11/17/kubernetes-from-the-ground-up-the-scheduler/)
24. Video \| [Jérôme Petazzoni - Cgroups, namespaces, and beyond: what are containers made from?](https://www.youtube.com/watch?v=sK5i-N34im8&feature=youtu.be)
25. Article \| [Brutally Honest Guide to Docker Graphdrivers](https://blog.jessfraz.com/post/the-brutally-honest-guide-to-docker-graphdrivers/)
26. Blog \| [Sumana Harihareshwara](https://www.harihareswara.net/ces.shtml)
27. Speech \| [Richard Hamming - You and Your Research](https://www.youtube.com/watch?v=a1zDuOPkMSw) [Transcript](https://www.cs.virginia.edu/~robins/YouAndYourResearch.html)
28. Book \| [Richard Hamming - The Art of Doing Science and Engineering](https://www.amazon.com/Art-Doing-Science-Engineering-Learning/dp/1732265178)
29. Blog \| [Paul Graham - Co-Founder of Y Combinator](http://paulgraham.com/)
30. Article \| [Paul Graham - Good and Bad Procrastination](http://www.paulgraham.com/procrastination.html)

## 2020-07-28

1. RTFM \| [Disabling Turbo Boost on AMD Laptops](https://www.kernel.org/doc/Documentation/cpu-freq/boost.txt)
2. Resource \| [Gary Explains: Rust: What is Ownership and Borrowing?](https://www.youtube.com/watch?v=79phqVpE7cU&feature=youtu.be)
3. Article \| [Adding a Volume Control to xmonad](http://dmwit.com/volume/)
4. Tool \| [Ghosd - Transparent System Notifications](http://neugierig.org/software/ghosd/)
5. Tool \| [Fusuma for Mouse Gestures in Linux](https://github.com/iberianpig/fusuma)
6. Tool \| [How to Use Fusuma](https://italolelis.com/posts/multitouch-gestures-ubuntu-fusuma/)
7. Thread \| [4 Rules to Getting Better](https://www.reddit.com/r/getdisciplined/comments/1q96b5/i_just_dont_care_about_myself/cdah4af/)

## 2020-07-27

1. Article \| [Najeem's article on Analysing Google Photos](https://medium.com/@najeem/analyzing-my-google-photos-library-with-python-and-pandas-bcb746c2d0f2)
2. RTFM \| [Linux Kernel Documentation](https://www.kernel.org/doc/html/)
3. Tool \| [Cubic is a tool to make customized Ubuntu or Linux Mint images](https://launchpad.net/cubic)
4. Tool \| [`ubuntu-mainline-kernel.sh` is a tool to update or manage the Kernel version with ease](https://github.com/pimlie/ubuntu-mainline-kernel.sh)
5. Tool \| [Drivers for TP-Link Wifi Dongles](https://github.com/lwfinger/rtl8188eu)
6. Tool \| [RyzenAdj is a tool to adjust AMD's Ryzen processor settings](https://github.com/FlyGoat/RyzenAdj)
7. Tool \| [`radeontop` is not quite `nvidia-smi` but it is something, for now](https://github.com/clbr/radeontop)
8. Thread \| [Trying to find `nvidia-smi` for AMD Radeon Cards](https://www.reddit.com/r/linuxquestions/comments/af8sdl/something_as_sophisticated_as_nvidiasmi_or_nvtop/)
9. Book \| [Tiny Python Projects](https://www.manning.com/books/tiny-python-projects?a_aid=bnpodcasts&utm_source=rss&utm_medium=rss#toc)
10. Article \| [Writing a file system in Rust](https://news.ycombinator.com/item?id=23967016)
11. Resource \| [Data Science Interview Questions in Python and SQL](https://news.ycombinator.com/item?id=23966752)
12. Course \| [Bartosz Milewski - School of Haskell](https://www.schoolofhaskell.com/user/bartosz/basics-of-haskell)
13. Course \| [Code and Exercises from Bartosz's School of Haskell](https://github.com/raviksharma/bartosz-basics-of-haskell)
14. Tool \| [Kardius - Find People Like You Near You](https://www.kardius.com/)
15. Thead \| [HN Comment on How CLIs Work](https://news.ycombinator.com/item?id=23960062)
16. Article \| [Sweet Expressions For Racket](https://github.com/takikawa/sweet-racket)
17. Course \| Coursera - Programming Languages [Course A](https://www.coursera.org/learn/programming-languages) \| [Course B](https://www.coursera.org/learn/programming-languages-part-b)
18. Tool \| [Racketlang is 25](https://news.ycombinator.com/item?id=23132621)
19. Thread \| [DashMap - Fast, Concurrent Hashmap in Rust](https://news.ycombinator.com/item?id=22699176)
20. Thread \| [A GPU Hash Table](https://news.ycombinator.com/item?id=22541925)
21. Book \| [A Job To Love](https://www.theschooloflife.com/shop/tsol-press-a-job-to-love/)
22. Article \| [What Should Truly Motivate Us At Work](https://www.theschooloflife.com/thebookoflife/what-should-truly-motivate-us-at-work/)
23. Tool \| [A Viewer for Git and Diff Output](https://github.com/dandavison/delta)
24. Article \| [Attack of Pythons : Gotchas](https://gist.githubusercontent.com/manojpandey/41b90cba1fd62095e247d1b2448ef85b/raw/0413c4805336b8030efc7de1e9fa0e229ca9903d/gotchas.md)
25. RTFM \| [Python Gotchas](https://docs.python-guide.org/writing/gotchas/#late-binding-closures)
26. Tool \| [Featuretools: Python Framework for Automated Feature Engineering](https://www.featuretools.com/)
27. Blog \| [Learning Rust in 2020](https://github.com/pretzelhammer/rust-blog/blob/master/posts/learning-rust-in-2020.md)
28. Course \| [Advent of Code is a bunch of programming exercises that are more fun than Leetcode, with annual sprints](https://adventofcode.com/)
29. Resource \| [BurntSushi's Rust Solutions to Advent of Code 2018](https://github.com/bcmyers/aoc2019)
30. Resource \| [bcmyers's Rust Solutions to Advent of Code 2019](https://github.com/bcmyers/aoc2019) \| [Youtube Livestream](https://www.youtube.com/watch?v=_JXpxmuR3ZE&feature=youtu.be&app=desktop#dialog)

## 2020-07-26

1. `arandr` is a great frontend for `xrandr`, a tool to set monitor configs in tiling window managers.
2. Debian Content Indices are interesting.]
3. The `sorted` function in Python has a `reverse` flag.
4. `collections.defaultdict` is amazing and has a slightly better performance than checking `{}.get`

## 2020-07-24

1. `pihole`'s Faster than light engine is a fork of dnsmasq
2. `argparse` *does* support sub-commands


## 2020-07-23

1. [It is possible to memoize dash callback responses with flask-caching](http://dash.plotly.com/testing)
2. pytest-dash has been abandoned since the official dash repo supports selenium via pytest now
3. Always ensure that the dash registration in a Flask-Dash app is configurable. Might want to not load dash when testing backend only.

# 2020-07-22

1. [Tips for faster Rust Compile Times](https://endler.dev/2020/rust-compile-times/)

## 2020-07-21

1. [pytest has a flag to hide traceback `--tb=no`, useful with `entr`](https://docs.pytest.org/en/stable/usage.html#modifying-python-traceback-printing)
2. [Testing Dash Applications using Pytest and Selenium](https://dash.plotly.com/testing)
3. [Al Sweigart - Scratch Course on Udemy](https://www.udemy.com/scratch-game-programming/)
4. [`kubectx` is a wrapper around `kubectl` and allows configuring namespaces](https://github.com/ahmetb/kubectx)
5. [Rust's Module System](http://www.sheshbabu.com/posts/rust-module-system/)
6. [How I write Backends](https://github.com/fpereiro/backendlore)
7. [Essays on Programmings](https://news.ycombinator.com/item?id=23903737)
8. [System Design for Advanced Beginners](https://robertheaton.com/2020/04/06/systems-design-for-advanced-beginners/)
9. [Alex Ellis's Blog](https://blog.alexellis.io/tag/raspberry-pi/)
10. [Made a 8-bit CPU](https://www.reddit.com/r/engineering/comments/huu38v/made_an_8bit_cpu_if_youve_ever_wondered_how_a/)
11. [Pi-Hole Unbound](https://docs.pi-hole.net/guides/unbound/)
12. [Pi-Hole Tips](https://www.reddit.com/r/pihole/comments/dezyvy/into_the_pihole_you_should_go_8_months_later/)
13. [Waveshare released a 7 color e-ink display](https://www.waveshare.com/5.65inch-e-paper-module-f.htm)
14. [Dijo - Terminal Habit Tracker written in Rust](https://github.com/NerdyPepper/dijo)
15. [Spotify TUI written in Rust](https://www.reddit.com/r/unixporn/comments/dekj2i/oc_a_spotify_terminal_user_interface_written_in/)
16. [Computer Productivity: Why it is important that software projects fail](https://www.berglas.org/Articles/ImportantThatSoftwareFails/ImportantThatSoftwareFails.html)

## 2020-07-20

1. [Python: `breakpoint` in empty `except` clause does not have access to the bound exception even if it is aliased](https://stackoverflow.com/questions/62796591/breakpoint-in-except-clause-doesnt-have-access-to-the-bound-exception)
2. [MIT OCW: Statistics for Applications](https://ocw.mit.edu/courses/mathematics/18-650-statistics-for-applications-fall-2016/lecture-videos/)
3. [Microsoft AI Lab](https://github.com/microsoft/ailab)
4. [Matplotlib for Google Maps](https://github.com/gmplot/gmplot)
5. [Github Coding Interview University](https://github.com/jwasham/coding-interview-university)
6. [ossu Computer Science Curriculum](https://github.com/ossu/computer-science)
7. [Awesome Interview Questions](https://github.com/MaximAbramchuck/awesome-interview-questions)
8. [The Book of Secret Knowledge (CLIs, tools, manuals, cheatsheets etc)](https://github.com/trimstray/the-book-of-secret-knowledge)
9. [Frontend Dev Bookmarks](https://github.com/dypsilon/frontend-dev-bookmarks)
10. [Patterns of Scalability](https://github.com/binhnguyennus/awesome-scalability)
11. [Awesome Design Tools](https://github.com/LisaDziuba/Awesome-Design-Tools)
12. [Awesome Shell](https://github.com/alebcay/awesome-shell)
13. [Awesome Remote Job](https://github.com/lukasz-madon/awesome-remote-job)
14. [Awesome VS Code](https://github.com/viatsko/awesome-vscode)
15. [Awesome Docker](https://github.com/veggiemonk/awesome-docker)
16. [Awesome Rust](https://github.com/rust-unofficial/awesome-rust)
17. [Awesome CSS Protips](https://github.com/AllThingsSmitty/css-protips)
18. [Space Vim](https://github.com/SpaceVim/SpaceVim)
19. [Awesome Penetration Test](https://github.com/enaqx/awesome-pentest)
20. [Awesome Design Resources](https://github.com/gztchan/awesome-design)
21. [Awesome Programming Falsehoods](https://github.com/kdeldycke/awesome-falsehood)
22. [Vim Galore](https://github.com/mhinz/vim-galore)
23. [Golang Bangalore Meetup 56](https://www.youtube.com/watch?v=KJRIR5vuNIQ)

## 2020-07-18

1. [Cyclomatic Complexity of Code or McCabe Complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
2. [mccabe is a Python module to analyse the McCabe's Complexity for a Python module or file](https://github.com/pycqa/mccabe)
4. [Python line-profiler](https://github.com/pyutils/line_profiler)
5. [Python Guppy / Heapy for Profiling Code](https://github.com/zhuyifei1999/guppy3)
6. [`entr` for running commands in posix systems when file(s) change](https://github.com/clibs/entr)
7. [pylint-flask](https://pypi.org/project/pylint-flask/)
8. [pylint-flask-sqlalchemy](https://pypi.org/project/pylint-flask-sqlalchemy/)
9. [windows terminal](https://github.com/microsoft/terminal)
10. [BangPypers Meetup Youtube Link - Code Quality, Interfaces, Complexity and Unit Testing](http://www.youtube.com/watch?v=eVYdPdvS2nQ)
11. [Python Static Code analysis with Prospector](http://prospector.landscape.io)
12. [Python isort for sorting imports automatically](https://pypi.org/project/isort/)
13. [Python Code Quality Authority](https://github.com/PyCQA)
14. [Python Quality Link by Abhiram](https://github.com/abhiramr/pyquality)
15. [CPython Internals RealPython Article by Anthony Shaw](https://realpython.com/cpython-source-code-guide/)
16. [CPython Internals Book by Anthony Shaw](https://realpython.com/products/cpython-internals-book/)
17. [Internals of CPython by Prashanth Raghu](https://intopythoncom.files.wordpress.com/2017/04/internalsofcpython3-6-1.pdf)
18. [Advanced Internals of CPython by Prashanth Raghu](https://intopythoncom.files.wordpress.com/2017/04/merged.pdf)
19. [Pablo Salgado - Soul of the Beast EuroPython 2019 Talk on CPython](https://www.youtube.com/watch?v=1_23AVsiQEc)
20. [CPython Internals Links](https://cpython-core-tutorial.readthedocs.io/en/latest/internals.html)
21. [CPython Internals: 10 Hour Codewalk through the Python Interpreter Source Code](http://pgbovine.net/cpython-internals.htm)
22. [Python Implements library](https://pypi.org/project/implements/)
23. [PEP 622 Structural Pattern Matching in Python](https://www.python.org/dev/peps/pep-0622/)
24. [Playground for PEP 622](https://mybinder.org/v2/gh/gvanrossum/patma/master?urlpath=lab/tree/playground-622.ipynb)
25. [Commitizen enforces how commit messages and changelogs are written](https://github.com/commitizen-tools/commitizen)
26. [PEP 618 Add Optional Length-Checking to zip](https://www.python.org/dev/peps/pep-0618/)
27. [Python Bytes #190: Anthony Shaw: Pylance is named after Sir Lancelot](https://pythonbytes.fm/episodes/show/190/you-will-now-be-notified-if-the-python-zipper-is-broken)
28. [Easier File Watching in Linux Hackaday Blog Post](https://hackaday.com/2019/01/31/linux-fu-easier-file-watching/)

## 2020-07-17

1. [Pickle's Nine Flaws](https://nedbatchelder.com/blog/202006/pickles_nine_flaws.html)
2. [Using the src folder with python](https://blog.ionelmc.ro/2014/05/25/python-packaging)
3. When mocking python functions in a flask test, ensure you reference the module where the function is called, not where it originates from.
4. [Flask-Security-Too includes common patterns for flask security](https://github.com/Flask-Middleware/flask-security/)
5. [PEP-508 is ... insanely detailed with what can be added to each line in requirements.txt](https://www.python.org/dev/peps/pep-0508/)
6. [Google Season of Docs is a program to get more people to contribute to documentation.](https://developers.google.com/season-of-docs)
7. [What Nobody Tells You about Documentation - the greatest video on how to structure docs that I have seen](https://www.youtube.com/watch?v=t4vKPhjcMZg)
8. [Divio's Documentation System - Amazing 4 Part System discussed in the video above](https://www.divio.com/blog/documentation/)
9. [docker-compose has *no* docstrings](https://github.com/docker/compose/blob/master/compose/cli/main.py)

## 2020-07-16

1. [MyPaint is MSPaint for Linux (not quite but more like PaintShopPro)](https://github.com/mypaint/mypaint)
2. [Jon Gjengset's Blog is a great resource. Check out his article on MIT6.824 and RAFT](https://thesquareplanet.com/)
3. [Jon Gjengset has a YouTube channel where he discusses intermediate Rust](https://www.youtube.com/channel/UC_iD0xppBwwsrM9DegC5cQQ)
4. [Crust of Rust on YouTube - Again, Jon Gjengset](https://youtu.be/rAl-9HwD858)
5. [OBS Project (Open Broadcaster Software) for recording and live-streaming, useful for my eventual youtube channel](https://obsproject.com/)
6. [PolyBar is a Status bar for i3m and Linux](https://github.com/polybar/polybar)
7. [xmonad is a tiling manager (like i3wm) but it uses haskell files for configs](https://xmonad.org/)
8. [Little Book of Rust Macros](https://danielkeep.github.io/tlborm/book/index.html)
9. [Book on Real World Cryptography](https://livebook.manning.com/book/real-world-cryptography/welcome/v-7/)
10. [Malicious SHA1](https://malicioussha1.github.io/)
11. [Understanding SHA Algorithms](https://www.maximintegrated.com/en/design/technical-documents/app-notes/7/7015.html)
12. [SHA256 Animation](https://github.com/in3rsha/sha256-animation)
13. [CS 61B Data Structures, Spring 2019](https://sp19.datastructur.es/)
14. [Semicolon&Sons Intermediate Screencasts](https://www.semicolonandsons.com/)
15. [Foundations of Applied Mathematics - Lots of Python and Data Science resources](https://foundations-of-applied-mathematics.github.io/)
16. [Missing Semester of Your CS Education](https://missing.csail.mit.edu/)
17. [Learn AI from Scratch](https://learnaifromscratch.github.io)
18. [Brown University: Programming and Programming Languages](https://papl.cs.brown.edu/2020/)
19. [Practical Object Oriented Design in Ruby - Sandi Metz](https://www.poodr.com/)

## 2020-07-15

1. [Common Lisp: A Gentle Introduction by David S. Touretzky is a great book on functional programming](https://www.cs.cmu.edu/~dst/LispBook/book.pdf)
2. [The Nokia N9 Alarm Clock app had a great design](http://nition.momentstudio.co.nz/2014/08/the-nokia-n9-alarm-clock/)
3. [Micro is a tiny editor for Linux](https://github.com/zyedidia/micro)
4. [Understanding and writing a JPEG decoder in Python](https://yasoob.me/posts/understanding-and-writing-jpeg-decoder-in-python/)
5. [pritunl is a simple home OpenVPN implentation](https://docs.pritunl.com/docs/installation)
6. [Resource for project based learning](https://github.com/tuvtran/project-based-learning)
7. [Succinct/compact/compressed data structures for data-intensive Python programs](https://github.com/miiohio/succinct)
8. [Jitsi for running your own self-hosted video call and chat](https://jitsi.org/)
9. [The Ethernet PAUSE frame](http://jeffq.com/blog/the-ethernet-pause-frame/)
10. [Flask's Method Views are so simple to implement. They're better for when the code gets really long](https://flask.palletsprojects.com/en/1.1.x/views/)
11. [Flask's' later docs seem to cover some insane stuff. Ex: Signals using the blinker library](https://flask.palletsprojects.com/en/1.1.x/signals/)

## 2020-07-14

1. [mkdocs-material is a real cool MaterialUI-based theme for mkdocs](https://squidfunk.github.io/mkdocs-material/)
2. [Gumshoe is a great scrolling effect for sidebars etc in vanilla JS](github.com/cfernandi/gumshoe)
3. [Barry Warsaw adapted the Zen of Python into a Song!]()
4. [Profiling Flask Apps using werkzeug.contrib.profiler.ProfilerMiddleware](https://gist.github.com/stonecharioteer/23cbba9f0a8ff7520cb07372dd56ef4a)
5. [What the heck is Pyproject.toml?](https://snarky.ca/what-the-heck-is-pyproject-toml/)
6. [Flit for Python](https://flit.readthedocs.io/en/latest/index.html)
7. [enscons is a library for building Python packages with SCons - the Software Construction Tool](https://bitbucket.org/dholth/enscons)
8. [SCons](https://scons.org/)
9. [Poetry for Python Projects - Manage environments for Python, as well as project dependency information.](https://github.com/python-poetry/poetry)
10. [`ss` is a tool to inspect sockets on Linux](https://www.redhat.com/sysadmin/dss-command)
11. [`sphinx-tabs` is a great way to add tabbed views in Sphinx](https://github.com/djungelorm/sphinx-tabs)
12. [The Baader-Meinhof Phenomenon or Frequency Illusion is when you discover something and see it everywhere](https://en.m.wikipedia.org/wiki/List_of_cognitive_biases#Frequency_illusion)

## 2020-07-13

1. [Flask-JWT-Extended has a great bunch of patterns and examples on expiring and blacklisting JWTs](https://flask-jwt-extended.readthedocs.io/en/stable/blacklist_and_token_revoking/)
2. [Learn Rust in the same way you'd learn Golang through the tour! This covers almost the entire Rust Book](https://tourofrust.com/)
3. [Real Python's article on Learn IP Address Concepts through Python](https://realpython.com/python-ipaddress-module/)
4. [Linux From Scratch is a great resource on learning Linux from first principles](http://www.linuxfromscratch.org/~bdubbs/cross2-lfs-book/index.html)
5. [Py-Spy is Top for Python!](https://github.com/benfred/py-spy)

## Older Items without Dates

1. [You Don't Know JS is one of the best resources on learning Javascript](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/README.md)
2. [ANTDesign (ANTD) is better than Material for React, IMO](https://github.com/ant-design/ant-design)
3. [cloc counts lines of code](https://github.com/AlDanial/cloc)
4. [cookiecutter can use Jinja to generate scaffolding for code](https://cookiecutter.readthedocs.io)
5. [fzf is amazing for searching through linux history](https://github.com/junegunn/fzf)
6. [Bat is better than the cat command.](https://github.com/sharkdp/bat)
7. [httpie is curl for humans](https://github.com/jakubroztocil/httpie)
8. [responses lets you mock requests calls safely](https://github.com/getsentry/responses)
9. [Run pytest in random order](https://github.com/jbasko/pytest-random-order)
10. [Let me google that for you](http://lmgtfy.com)
11. [Limyaeel's Rants are the best commentary on the Fantasy fiction tropes](https://curiosityquills.com/limyaael/)
12. [Tokei is better than cloc](https://github.com/XAMPPRocky/tokei)
13. [ripgrep is grep on steroids](https://github.com/BurntSushi/ripgrep)
14. `python -m http.server`, this needs no link.
15. [youtube-dl allows you to download youtube videos easily and convert them](https://github.com/ytdl-org/youtube-dl)
16. [GUI for youtube-dl](https://github.com/MrS0m30n3/youtube-dl-gui)
17. [node's live-server module is good for live reloading static html](https://github.com/tapio/live-server)
18. [Tech conferences in India](https://github.com/nikhita/tech-conferences-india)
19. [Secure Headers for Flask and other Python Web Frameworks](https://secure.readthedocs.io/en/latest/)
20. [Use Bandit for security in python applications](https://github.com/PyCQA/bandit)
21. [pre-commit allows you to setup version control for your hooks](https://pre-commit.com/)
22. [fast-api is asynchronous flask on steroids](https://fastapi.tiangolo.com/)
23. [Armin Ronacher's Blog](https://lucumr.pocoo.org/)
24. [Ned Batchelder's Blog - Is Python Interpreted or Compiled? Yes.](https://nedbatchelder.com/blog/201803/is_python_interpreted_or_compiled_yes.html)
25. [The first 4 bytes of every Java class file has the magic value 0xCAFEBABE](https://www.artima.com/insidejvm/whyCAFEBABE.html)
26. [Compiling Python Code](https://docs.python.org/3/library/codeop.html)
27. [`byteplay` - play with python bytecode](https://wiki.python.org/moin/ByteplayDoc)
28. [Raymond Hettinger's Blog](https://rhettinger.wordpress.com/)
29. [Real Python PyGame Primer](https://realpython.com/pygame-a-primer/)
30. [Rust By Example](https://doc.rust-lang.org/stable/rust-by-example/)
31. [Core Algorithms Deployed - Stack Overflow Question](https://cstheory.stackexchange.com/questions/19759/core-algorithms-deployed/19773#19773)
32. [`revel` Web Framework for Go](https://revel.github.io/)
33. [Build Web Application with Golang Astaxie](https://astaxie.gitbooks.io/build-web-application-with-golang/en/02.7.html)
34. [Complete Guide to `calc()` in CSS](https://css-tricks.com/a-complete-guide-to-calc-in-css/)
35. [Matt Mullenweg on Remote Work](https://www.nytimes.com/2020/07/12/business/matt-mullenweg-automattic-corner-office.html)
36. [The Importance of Deep Work and the 30-hour method for learning a new skill](https://azeria-labs.com/the-importance-of-deep-work-the-30-hour-method-for-learning-a-new-skill/)
37. [Functional Light Javascript](https://github.com/getify/Functional-Light-JS/blob/master/manuscript/foreword.md)
38. [Professor Frisby's Mostly Adequate Guide to Functional Programming](https://github.com/MostlyAdequate/mostly-adequate-guide)
39. [Front End Developer Handbook](https://frontendmasters.com/books/front-end-handbook/2019/#1)
40. [The CSS "Ah-ha!" moment](https://css-tricks.com/the-css-ah-ha-moment/)
41. [What does a Well-Documented CSS Codebase Look Like?](https://css-tricks.com/well-documented-css-codebase-look-like/)
42. [The moment CSS started making "Sense"](https://css-tricks.com/moment-css-started-making-sense/)
43. [Multi-Line Padded Text](https://css-tricks.com/multi-line-padded-text/)
44. [Don't Overthink It Grids](https://css-tricks.com/dont-overthink-it-grids/)
45. [CSS Zen Garden](http://www.csszengarden.com/)
46. [The Anatomy of a Reference Site Component Detail Page](https://bradfrost.com/blog/post/anatomy-of-a-pattern-in-a-pattern-library/)
47. [Taking the Pattern Library to the Next Level](https://www.smashingmagazine.com/taking-pattern-libraries-next-level/)
48. [W3C Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG20/)
49. [HTML5 for Web Designers](https://html5forwebdesigners.com/)
50. [CSS Pseudo-Classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)
51. [Javascript Questions](https://github.com/lydiahallie/javascript-questions)
52. [Pika cdn for npm](https://www.pika.dev/cdn)
53. [Joy of Elixir](https://joyofelixir.com/)
54. [Waterline.js ORM for Node](https://waterlinejs.org/)
55. [Conflict-Free Replicated Data Type (CRDT)](https://en.m.wikipedia.org/wiki/Conflict-free_replicated_data_type)
56. [Nerves IoT Platform](https://www.nerves-project.org/)
57. [Grok the GIL: How to Write Fast and Thread-Safe Python](https://opensource.com/article/17/4/grok-gil)
58. [How Does `asyncio` work?](https://stackoverflow.com/questions/49005651/how-does-asyncio-actually-work/51116910#51116910)
59. [Using `multiprocessing.Process` with a maximum number of simultaneous processes](https://stackoverflow.com/questions/20886565/using-multiprocessing-process-with-a-maximum-number-of-simultaneous-processes)
60. [Designing a delightful command line interface](https://devrel.net/developer-experience/designing-a-delightful-command-line-interface)
61. [Introducing Linux Network Namespaces](https://blog.scottlowe.org/2013/09/04/introducing-linux-network-namespaces/)
62. [Wagtail CMS and Site Framework](https://docs.wagtail.io/en/v2.6.1/getting_started/tutorial.html)
63. [Django Class Based Views](https://docs.djangoproject.com/en/2.2/topics/class-based-views/intro/)
64. [Nina Zakharenko - The Ultimate Guide to Memorable Tech Talks](https://medium.com/@nnja/the-ultimate-guide-to-memorable-tech-talks-e7c350778d4b)
65. [Intermediate Vim](https://www.hillelwayne.com/post/intermediate-vim/)
66. [Learn Rust the Dangerous Way](http://cliffle.com/p/dangerust/)
67. [Debugging Memory on Linux](https://www.linuxjournal.com/article/4681)
68. [Nathan Grigg's Blog - Vim and Linux](https://nathangrigg.com/)
69. [ELI5: What is Virtual Memory? Why do we Need it?](https://www.reddit.com/r/explainlikeimfive/comments/kpoz3/eli5_what_is_virtual_memory_why_we_need_it/)
70. [Python Design Patterns](https://python-patterns.guide/)
71. [Problems in Rust Adoption](https://sanxiyn.blogspot.com/2016/06/problem-in-rust-adoption.html?m=1)
72. [The Paging Game - Game on Learning the Virtual Memory Paging Process](https://en.m.wikisource.org/wiki/The_Paging_Game)
73. [What is RabbitMQ?](https://www.erlang-solutions.com/blog/an-introduction-to-rabbitmq-what-is-rabbitmq.html)
74. [The Turing Pi - Raspberry Pi Compute Node Cluster](https://turingpi.com/)
75. [Generate Fake Data in Python using `mimesis`](https://github.com/lk-geimfari/mimesis)
76. [Setting up K3S with Cluster Monitoring on the Raspberry Pi](https://github.com/carlosedp/)
