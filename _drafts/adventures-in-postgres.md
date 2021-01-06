# Adventures in PostgreSQL

This is an article wherein I describe my adventures with learning how to use postgresql properly.

I wanted to learn how to profile and use postgresql like a boss. So I sshed into my Raspberry Pi Zero W which is currently running `pihole`,
  and I git cloned `git://git.postgresql.org/git/postgresql.git`, the source code for PostgresQL.


# Goals

1. Build from source on a Rasberry Pi Zero W running a pretty old MicroSD Card (Class 10).
2. Build in a custom user.
3. Build in a separate folder
4. Install in non-standard directory.
5. Keep data in non-standard directory.
6. Manually make systemctl file.
7. Run at boot
8. Run on non-standard port
9. Make a database with 10 GB of fake data.
10. Replicate a "github" + "bitbucket" database.
11. Run queries.
12. Cached views.
13. Time views.


## Installation

start time: 2020-12-11 19:30

First, cloning the source code. Boy this took quite some time. I was able to download the code fast enough, but it took *ages* to resolve the deltas.
After this, the next task was to switch to a particular tag. I am learning PostgreSQL v12, and as of this article, the current version is v13.
I'd like to stay a bit safe.


```bash
$ time git clone git://git.postgresql.org/git/postgresql.git

real    20m17.823s
user    15m49.335s
sys     1m17.781s

```


Dependencies:

Install these: bison, libreadline-dev, flex


## Configuration

I wanted to build in a separate directory.

```bash
$ mkdir -p $HOME/build_dir
$ cd $HOME/build_dir
$ time $HOME/postgresql/configure --prefix=$HOME/install_dir

real    3m51.631s
user    2m22.513s
sys     1m12.188s

```


```bash
$ time make all

```
