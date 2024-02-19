#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o xtrace
set -o pipefail
timestamp=$(date +%T)
timestamp=$(date -u +%Y-%m-%dT%H:%M:%S%Z)
echo "Starting changes at $timestamp" >> $HOME/.local/incrontab.log
poetry run sphinx-build -M $@ "$PWD/source" "$PWD/build/" $(0) 2>&1 | tee $PWD/sphinx.log 
timestamp=$(date -u +%Y-%m-%dT%H:%M:%S%Z)
echo $(pwd) >> $HOME/.local/incrontab.log
echo "Completed changes at $timestamp" >> $HOME/.local/incrontab.log
