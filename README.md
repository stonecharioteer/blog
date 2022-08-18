# stonecharioteer.com

[![Publish Github Pages](https://github.com/stonecharioteer/blog/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/stonecharioteer/blog/actions/workflows/gh-pages.yml)

This is the sphinx-based source code for my [blog](https://stonecharioteer.com).

To build this using gh-actions, I recommend starting a runner using docker. I
prefer running the runner locally instead of using a cloud runner.

```bash
    docker run -d --name blog-runner --rm --pull=always -e RUNNER_WORK_DIR=/tmp/runner/ \
        -e RUNNER_NAME=$RUNNER_NAME -e GITHUB_ACCESS_TOKEN=$ACCESS_TOKEN -e RUNNER_REPOSITORY_URL=$REPO_URL \
        -v /tmp/runner:/tmp/runner--rm tcardonne/github-runner:ubuntu-20.04
```

Set the values of those envvars using `direnv`, it makes things easy.

Don't build this locally, it's annoying. But if you have to, use `ablog clean && ablog build``


## Categories

- Health
- Personal
- Reading
- Show and Tell
- Tech
- Updates
- Writing

## Tags

I'm going to use these tags:

- ADHD
- Advent of Code
- Algorithms
- Ansible
- Arduino
- BangPypers
- Bipolar Disorder
- Career Advice
- Conda
- Conferences
- Covid-19
- Data Structures
- Developer Experience
- Developer Relations
- Development Environment
- Django
- Docker
- Documentation
- Dotfiles
- Electronics
- Empathy
- Fiction
- Flask
- Focus
- Furo
- Goals
- Golang
- GopherCon
- Hearing Loss
- Hobbies
- Hugo
- K3s
- Kubernetes
- Leadership
- Learning
- Leetcode
- Libraries
- Mechanical Keyboards
- Meetups
- Mental Health
- Merkle Science
- Meta
- Microk8s
- Minikube
- Mythology
- Neovim
- Nostalgia
- Notes
- Oso
- Philosophy
- Podcasts
- Podman
- Programming
- PyCon
- Pyenv
- Python
- Rabbit Hole
- RabbitMQ
- Raspberry Pi
- Rust
- Screencast
- Security
- Single-Sided Deafness
- Sphinx
- Statistics
- TIL
- Teaching
- Technical Interviews
- Thoughts
- Travel
- Typing
- Ubuntu
- Vagrant
- Vim
- Virtualenv
- Visa
- Web Development
- Zen
