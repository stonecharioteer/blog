:blogpost: true
:category: Tech
:tags: vagrant, dev-setup
:date: Jan 10, 2022

============================
Vagrant
============================

I'm late to the Vagrant train. I must have heard about it in 2014, but I've
never bothered to look it up. I'm using it lately to test out my dotfiles, which
I'm creating Ansible playbooks for. It's convenient.

For those of you who're either too young to have encountered it, or have never
heard of it before, Vagrant is a tool that allows you to create a text-based
configuration to spin up virtual machines. These machines can be spun up and
destroyed at whim, and you will always get an identical machine as long as your
configuration is defined and you do not install adhoc stuff directly without
recording it in the config.

I'm not delving too deep into it, but all I need to know is how to provision
a few machines with IPs I can communicate with using Ansible.

.. code:: ruby

    Vagrant.configure("2") do |config|
      config.vm.define "ubuntu1" do |ubuntu1|
        ubuntu1.vm.box = "hashicorp/bionic64"
        ubuntu1.vm.host_name = "ubuntu1804"
        ubuntu1.vm.network "private_network", ip: "192.168.60.2"
      end

      config.vm.define "ubuntu2" do |ubuntu2|
        ubuntu2.vm.box = "bento/ubuntu-21.04"
        ubuntu2.vm.host_name = "ubuntu2104"
        ubuntu2.vm.network "private_network", ip: "192.168.60.3"
      end

      config.vm.define "arch1" do |arch1|
        arch1.vm.box = "archlinux/archlinux"
        arch1.vm.host_name = "archbtw"
        arch1.vm.network "private_network", ip: "192.168.60.4"
      end

    end

In this file, I'm defining 3 virtual machines: 2 Ubuntu boxes and 1 archlinux
box. Each of the machines gets a unique IP address from a subnet I don't use in
my local network. I've not yet figured out how to enable host-name broadcasting
locally, so I refer to them in my Ansible hosts file with the IP address
hard-coded in. This works fine for testing.

I bring up the machines with: ``vagrant up``, and whenever I want fresh
machines, I use ``vagrant destroy -f && vagrant up``. If I were to change the
config, the ``Vagrantfile``, I'd just run ``vagrant reload --provision``.

There's something to be said about learning *only what you need* in today's
world, so this is all I'm learning about Vagrant. It helps me test out my
Ansible playbooks so I'm happy there. I've looked at the provisioning
commands as well, but I don't need those right now. I'm happier running the
commands externally through Ansible instead of telling the Vagrantfile to
run my playbooks. Call it separation of concerns or standardized usage, if you
will.
