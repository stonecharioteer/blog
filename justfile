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
  rm -rf build
  docker build -t sphinx-docs .
  docker rm sphinx-docs-container || echo "Didn't need to cleanup container"
  docker run --name sphinx-docs-container sphinx-docs
  docker cp sphinx-docs-container:/app/build ./build
  docker rm sphinx-docs-container


# watch directory for file changes and rebuild. note, you'll have to rerun this command if you add new files/folders to be watched.
build-watch:
  # fd --type file | entr just build
  watchexec --watch source/ --debounce 2000 --clear --notify -- just build

# run github actions runner
gh-runner:
  docker run -d --name blog-runner --rm --pull=always -e RUNNER_WORK_DIR=/tmp/runner/ \
    -e RUNNER_NAME=$RUNNER_NAME -e GITHUB_ACCESS_TOKEN=$GITHUB_ACCESS_TOKEN -e RUNNER_REPOSITORY_URL=$REPO_URL \
    -v /tmp/runner:/tmp/runner--rm tcardonne/github-runner:ubuntu-20.04

# serve build folder using live-server
serve:
  live-server --host "0.0.0.0" --port 8001 build/html

build-resume:
  rst2pdf -o source/resume/resume.pdf source/resume/resume.rst

release-resume: build-resume
  cp source/resume/resume.pdf "/tmp/vinay-keerthi-resume-v$(date +%F).pdf"
  gh release create "v$(date -u +%Y.%m.%d)" "/tmp/vinay-keerthi-resume-v$(date +%F).pdf"

# Recipe to call the create_book.sh script with arguments
create-book *ARGS:
    ./scripts/create-book.sh {{ARGS}}
