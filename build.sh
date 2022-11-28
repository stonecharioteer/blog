#!/usr/bin/env bash
timestamp=$(date +%T)
timestamp=$(date -u +%Y-%m-%dT%H:%M:%S%Z)
echo "Starting changes at $timestamp" >> $HOME/.local/incrontab.log
# cd $HOME/code/checkouts/code/personal/blog/ && source ~/.python/venvs/py3.9/blog/bin/activate && make html >> $HOME/.local/incrontab.log 2>&1
~/.python/venvs/py3.9/blog/bin/sphinx-build -a ~/code/checkouts/personal/blog/source ~/code/checkouts/personal/blog/build/html >> $HOME/.local/incrontab.log 2>&1
timestamp=$(date -u +%Y-%m-%dT%H:%M:%S%Z)
echo $(pwd) >> $HOME/.local/incrontab.log
echo "Completed changes at $timestamp" >> $HOME/.local/incrontab.log
