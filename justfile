set shell := ["bash", "-uc"]
default: (build)
alias b:= build
alias bw:= build-watch
alias gh:= gh-runner
alias s:= serve
set dotenv-load

# install python correctly
install-python:
  echo "TODO" 1>&2
  exit 1

# build the blog locally
build:
  ./build.sh html

# watch directory for file changes and rebuild. note, you'll have to rerun this command if you add new files/folders to be watched.
build-watch:
  fd --type file | entr just build

# run github actions runner
gh-runner:
  docker run -d --name blog-runner --rm --pull=always -e RUNNER_WORK_DIR=/tmp/runner/ \
    -e RUNNER_NAME=$RUNNER_NAME -e GITHUB_ACCESS_TOKEN=$GITHUB_ACCESS_TOKEN -e RUNNER_REPOSITORY_URL=$REPO_URL \
    -v /tmp/runner:/tmp/runner--rm tcardonne/github-runner:ubuntu-20.04

# serve build folder using live-server
serve:
  live-server -h "0.0.0.0" build/html

build-resume:
  rst2pdf -o source/resume/resume.pdf source/resume/resume.rst

release-resume: build-resume
  gh release create "v$(date -u +%Y.%m.%d)" source/resume/resume.pdf
