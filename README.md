# stonecharioteer.com

This is the sphinx-based source code for my [blog](https://stonecharioteer.com).

To build this using gh-actions, I recommend starting a runner using docker. I
prefer running the runner locally instead of using a cloud runner.

```bash
    docker run -d -e RUNNER_NAME= -e RUNNER_WORKDIR=/tmp/runner -e ACCESS_TOKEN= -e REPO_URL= -v /tmp/runner:/tmp/runner myoung34/github-runner:ubuntu-bionic
```
Set the values of those envvars using `direnv`, it makes things easy.

Don't build this locally, it's annoying. But if you have to, use `ablog clean && ablog build``


## Categories

- Health
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
- Flask
- Focus
- Goals
- Golang
- GopherCon
- Hearing Loss
- Hobbies
- K3s
- Kubernetes
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
- Hugo
- Furo
