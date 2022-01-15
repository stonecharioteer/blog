# stonecharioteer.com

This is the sphinx-based source code for my [blog](https://stonecharioteer.com).

To build this using gh-actions, I recommend starting a runner using docker. I
prefer running the runner locally instead of using a cloud runner.

```bash
    docker run -d -e RUNNER_NAME= -e RUNNER_WORKDIR=/tmp/runner -e ACCESS_TOKEN= -e REPO_URL= -v /tmp/runner:/tmp/runner myoung34/github-runner:ubuntu-bionic
```
Set the values of those envvars using `direnv`, it makes things easy.

Don't build this locally, it's annoying. But if you have to, use `ablog clean && ablog build``
